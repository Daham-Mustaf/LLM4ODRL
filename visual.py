import matplotlib.pyplot as plt
import numpy as np

# Data preparation
labels = ['Use_Case_1', 'Use_Case_2', 'Use_Case_3', 'Use_Case_4', 
          'Use_Case_5', 'Use_Case_6', 'Use_Case 7', 'Use_Case 8', 'Use_Case 9', 
          'Use_Case_10', 'Use_Case_11', 'Use_Case_12']

# Scores for each model
gpt_3_5_scores = {
    'Ontology-Guided': [6, 4, 5, 9, 7, 5, 9, 5, 8, 6, 5, 10],
    'OSES Insights': [10, 9, 15, 11, 15, 7, 13, 10, 12, 9, 10, 10],
    'Refinement': [13, 15, 19, 15, 19, 13, 15, 14, 17, 11, 11, 12],
    'total scores': [22, 22, 22, 22, 20, 20, 20, 20, 20, 16, 16, 16]
}

gpt_4_scores = {
    'Ontology-Guided': [6, 5, 5, 11, 10, 7, 4, 9, 7, 9, 4, 8],
    'OSES Insights': [11, 18, 19, 17, 16, 17, 16, 16, 15, 9, 11, 11],
    'Refinement': [15, 21, 21, 19, 19, 18, 20, 20, 20, 14, 14, 14],
    'total scores': [22, 22, 22, 22, 20, 20, 20, 20, 20, 16, 16, 16]
}

gpt_4o_scores = {
    'Ontology-Guided': [11, 10, 13, 12, 12, 9, 4, 7, 9, 8, 9, 10],
    'OSES Insights': [13, 14, 15, 15, 15, 14, 18, 17, 16, 9, 9, 11],
    'Refinement': [16, 21, 20, 21, 18, 19, 20, 19, 20, 14, 14, 15],
    'total scores': [22, 22, 22, 22, 20, 20, 20, 20, 20, 16, 16, 16]
}

x = np.arange(len(labels))  # the label locations
# width = 0.2  # the width of the bars

# fig, ax = plt.subplots(figsize=(15, 8))
# rects1 = ax.bar(x - width, gpt_3_5_scores['total scores'], width, label='GPT-3.5-turbo')
# rects2 = ax.bar(x, gpt_4_scores['total scores'], width, label='GPT-4')
# rects3 = ax.bar(x + width, gpt_4o_scores['total scores'], width, label='GPT-4o')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_xlabel('Categories')
# ax.set_ylabel('Scores')
# ax.set_title('Scores by Category and Model')
# ax.set_xticks(x)
# ax.set_xticklabels(labels, rotation=45, ha="right")
# ax.legend()

# fig.tight_layout()

# plt.show()
# fig, ax = plt.subplots(figsize=(15, 8))

# # Plotting lines for GPT-3.5-turbo
# ax.plot(labels, gpt_3_5_scores['Ontology-Guided'], marker='o', label='GPT-3.5-turbo Ontology-Guided')
# ax.plot(labels, gpt_3_5_scores['OSES Insights'], marker='o', label='GPT-3.5-turbo OSES Insights')
# ax.plot(labels, gpt_3_5_scores['Refinement'], marker='o', label='GPT-3.5-turbo Refinement')
# ax.plot(labels, gpt_3_5_scores['total scores'], marker='o', label='GPT-3.5-turbo Total Scores')

# # Plotting lines for GPT-4
# ax.plot(labels, gpt_4_scores['Ontology-Guided'], marker='s', label='GPT-4 Ontology-Guided')
# ax.plot(labels, gpt_4_scores['OSES Insights'], marker='s', label='GPT-4 OSES Insights')
# ax.plot(labels, gpt_4_scores['Refinement'], marker='s', label='GPT-4 Refinement')
# ax.plot(labels, gpt_4_scores['total scores'], marker='s', label='GPT-4 Total Scores')

# # Plotting lines for GPT-4o
# ax.plot(labels, gpt_4o_scores['Ontology-Guided'], marker='^', label='GPT-4o Ontology-Guided')
# ax.plot(labels, gpt_4o_scores['OSES Insights'], marker='^', label='GPT-4o OSES Insights')
# ax.plot(labels, gpt_4o_scores['Refinement'], marker='^', label='GPT-4o Refinement')
# ax.plot(labels, gpt_4o_scores['total scores'], marker='^', label='GPT-4o Total Scores')

# ax.set_xlabel('Use Cases')
# ax.set_ylabel('Scores')
# ax.set_title('Scores by Use Cases and LLM Models')
# ax.set_xticks(x)
# ax.set_xticklabels(labels, rotation=45, ha="right")
# ax.legend()

# fig.tight_layout()
# plt.savefig('score.svg', format='svg')

# plt.show()


fig, ax = plt.subplots(figsize=(15, 8))

# Plotting lines for GPT-3.5-turbo
ax.plot(labels, gpt_3_5_scores['Ontology-Guided'], marker='o', label='GPT-3.5-turbo Ontology-Guided')
ax.plot(labels, gpt_3_5_scores['OSES Insights'], marker='o', label='GPT-3.5-turbo OSES Insights')
ax.plot(labels, gpt_3_5_scores['Refinement'], marker='o', label='GPT-3.5-turbo Refinement')
ax.plot(labels, gpt_3_5_scores['total scores'], marker='o', label='GPT-3.5-turbo Total Scores')

# Plotting lines for GPT-4
ax.plot(labels, gpt_4_scores['Ontology-Guided'], marker='s', label='GPT-4 Ontology-Guided')
ax.plot(labels, gpt_4_scores['OSES Insights'], marker='s', label='GPT-4 OSES Insights')
ax.plot(labels, gpt_4_scores['Refinement'], marker='s', label='GPT-4 Refinement')
ax.plot(labels, gpt_4_scores['total scores'], marker='s', label='GPT-4 Total Scores')

# Plotting lines for GPT-4o
ax.plot(labels, gpt_4o_scores['Ontology-Guided'], marker='^', label='GPT-4o Ontology-Guided')
ax.plot(labels, gpt_4o_scores['OSES Insights'], marker='^', label='GPT-4o OSES Insights')
ax.plot(labels, gpt_4o_scores['Refinement'], marker='^', label='GPT-4o Refinement')
ax.plot(labels, gpt_4o_scores['total scores'], marker='^', label='GPT-4o Total Scores')

ax.set_xlabel('Use Cases')
ax.set_ylabel('Scores')
ax.set_title('Scores by Use Cases and LLM Models')
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=45, ha="right")

# Adjusting legend to be inside the plot without overlapping
ax.legend(loc='best', fontsize='small')

fig.tight_layout()
plt.savefig('score.svg', format='svg')

plt.show()

# from math import pi

# # Prepare data for radar chart
# categories = ['Ontology-Guided', 'OSES Insights', 'efinement', 'total scores']
# N = len(categories)

# # Data for radar
# values_gpt_3_5 = [np.mean(gpt_3_5_scores[cat]) for cat in categories]
# values_gpt_4 = [np.mean(gpt_4_scores[cat]) for cat in categories]
# values_gpt_4o = [np.mean(gpt_4o_scores[cat]) for cat in categories]

# # Repeat the first value to close the radar chart
# values_gpt_3_5 += values_gpt_3_5[:1]
# values_gpt_4 += values_gpt_4[:1]
# values_gpt_4o += values_gpt_4o[:1]

# angles = [n / float(N) * 2 * pi for n in range(N)]
# angles += angles[:1]

# fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# ax.set_theta_offset(pi / 2)
# ax.set_theta_direction(-1)

# plt.xticks(angles[:-1], categories)

# ax.plot(angles, values_gpt_3_5, marker='o', label='GPT-3.5-turbo')
# ax.fill(angles, values_gpt_3_5, 'b', alpha=0.1)

# ax.plot(angles, values_gpt_4, marker='s', label='GPT-4')
# ax.fill(angles, values_gpt_4, 'r', alpha=0.1)

# ax.plot(angles, values_gpt_4o, marker='^', label='GPT-4o')
# ax.fill(angles, values_gpt_4o, 'g', alpha=0.1)

# plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# plt.show()


