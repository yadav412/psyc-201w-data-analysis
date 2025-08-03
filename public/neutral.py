import pandas as pd
from scipy.stats import f_oneway

# Load Excel file and sheets
file_path = "neut.xlsx"  
xls = pd.ExcelFile(file_path)
video1_df = xls.parse('Video 1')
video2_df = xls.parse('Video 2')

# Clean column headers
columns = video1_df.iloc[1].tolist()
columns[0] = "Participant"
columns[1] = "Group"
columns = [str(col) for col in columns]

# Prepare dataframes
video1_clean = video1_df.iloc[2:].copy()
video1_clean.columns = columns
video1_clean["Video"] = "Video 1"

video2_clean = video2_df.iloc[2:].copy()
video2_clean.columns = columns
video2_clean["Video"] = "Video 2"

combined_df = pd.concat([video1_clean, video2_clean], ignore_index=True)

# Convert emotion columns to numeric
emotion_columns = columns[2:]
combined_df[emotion_columns] = combined_df[emotion_columns].apply(pd.to_numeric, errors='coerce')

# Drop rows with too many missing emotion scores
combined_df.dropna(subset=emotion_columns, thresh=int(len(emotion_columns) * 0.75), inplace=True)

# Perform ANOVA and calculate effect size (eta-squared)
anova_results = []
for emotion in emotion_columns:
    group1 = combined_df[combined_df["Video"] == "Video 1"][emotion].dropna()
    group2 = combined_df[combined_df["Video"] == "Video 2"][emotion].dropna()

    if len(group1) > 1 and len(group2) > 1:
        f_stat, p_val = f_oneway(group1, group2)
        df_between = 1
        df_within = len(group1) + len(group2) - 2
        eta_squared = (f_stat * df_between) / (f_stat * df_between + df_within)

        # Interpret effect size
        if eta_squared < 0.01:
            interpretation = 'Very small'
        elif eta_squared < 0.06:
            interpretation = 'Small'
        elif eta_squared < 0.14:
            interpretation = 'Medium'
        else:
            interpretation = 'Large'

        anova_results.append({
            "Emotion": emotion,
            "F-statistic": round(f_stat, 3),
            "p-value": round(p_val, 4),
            "Eta-squared": round(eta_squared, 4),
            "Effect Size": interpretation
        })

# Output as DataFrame
anova_df = pd.DataFrame(anova_results)
anova_df.sort_values("p-value", inplace=True)
print(anova_df)

group_stats = combined_df.groupby("Video")[emotion_columns].agg(['mean', 'std'])

# Flatten the multi-index columns
group_stats.columns = ['_'.join(col).strip() for col in group_stats.columns.values]
group_stats.reset_index(inplace=True)

# Show the stats
print("\n=== Emotion Means and Standard Deviations by Video ===")
print(group_stats)


group_stats = combined_df.groupby("Video")[emotion_columns].agg(['mean', 'std'])

# Flatten the multi-index columns
group_stats.columns = ['_'.join(col).strip() for col in group_stats.columns.values]
group_stats.reset_index(inplace=True)



print("\n=== Emotion Means and Standard Deviations by Video (Detailed) ===")

for emotion in emotion_columns:
    video1_vals = combined_df[combined_df["Video"] == "Video 1"][emotion].dropna()
    video2_vals = combined_df[combined_df["Video"] == "Video 2"][emotion].dropna()
    
    mean1 = video1_vals.mean()
    std1 = video1_vals.std()
    mean2 = video2_vals.mean()
    std2 = video2_vals.std()
    
    print(f"\nEmotion: {emotion}")
    print(f"  Video 1 - Mean: {mean1:.3f}, Std: {std1:.3f}")
    print(f"  Video 2 - Mean: {mean2:.3f}, Std: {std2:.3f}")
