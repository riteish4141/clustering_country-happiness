import pandas as pd
from sklearn.feature_selection import RFE
import plotly.graph_objs as go
from plotly.offline import iplot, download_plotlyjs
import plotly
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


class Clustering:

    def __init__(self, data):
        self.data = data

    def load_data(self):
        data = pd.read_csv(self.data, header=0)
        return data

    def data_processing(self):
        data = self.load_data()
        interested_features = data.columns.values.tolist()[1:]
        data_x = data[interested_features]
        country = data[data.columns[0]]
        #print("country is; \n",country)
        final_data =data.iloc[:,2:]  # remove country and happiness score feature
        return final_data

    # def data_visualisation(self):
    #     """if notebook is being used, use this way of visualisation"""
    #     data = self.load_data()
    #     data_toplot = dict(type='choropleth',
    #                 locations=data['Country'],
    #                 locationmode='country names',
    #                 z=data['Happiness.Rank'],
    #                 text=data['Country'],
    #                 colorbar={'title': 'Happiness'})
    #     layout = dict(title='Global Happiness',
    #                   geo=dict(showframe=False,
    #                            projection={'type': 'Mercator'}))
    #     choromap3 = go.Figure(data=[data_toplot], layout=layout)
    #     x = iplot(choromap3)
    #     plotly.offline.plot(x , filename='file.html')

    def data_visualisation(self):
        data = self.load_data()
        yaxis = data['Happiness.Rank']
        plt.scatter(data['Economy..GDP.per.Capita.'], yaxis)
        plt.scatter(data['Health..Life.Expectancy.'], yaxis)
        plt.scatter(data['Dystopia.Residual'], yaxis)
        plt.show()


def main():
    clustering = Clustering(data="2017.csv")
    features = clustering.data_processing()

if __name__ == '__main__':
    main()