from webscrapers import Focus
import matplotlib.pyplot as plt

# focus = FocusIPCA(r'/Users/gustavoamarante/Desktop/chromedriver')
focus = Focus(r'C:/Users/mathe/Downloads/chromedriver_win32/chromedriver.exe')

df = focus.scrape(indicator='pib', initial_date='2018-01-01', end_date='2021-12-31', frequency='quarterly')

df.plot()
plt.show()
a = 2


