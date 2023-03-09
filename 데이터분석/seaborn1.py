import seaborn as sns # 그래프

# 1. 경향성 표현하기
sns.set_theme(style='whitegrid')
penguins = sns.load_dataset("penguins").dropna()
# print(penguins)

# lineplot => 어떤 지표가 커짐에 따라서, 나머지가 어떻게 변화하는지, 시간에 따른 변화량 볼때등등

result = sns.lineplot(data=penguins, x="body_mass_g", y="flipper_length_mm", ci=None) # 질량에 따른 발사이즈 변화 hue="species" 종에따라 색깔다르게
print(result)
# pointplot => 특정 수치 데이터를 에러 바와 함꼐 출력해주는 plot