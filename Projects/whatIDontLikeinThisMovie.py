"""
dic1
dict2

        movie name
pros             cons                       what is missing/place to improve
tech is good        violence, blood
strong narration

list
dict[movie1, MovieAttributes]
"""
thisdict = {


}
movieMeta = []

class MovieMetaInfo:
    allMovies = {

    }
    def __init__(self, releaseyear, _moviename):
        self.releaseYear = releaseyear
        self.movieName = _moviename
        self.uniqueId = str(releaseyear) +'_'+ str(_moviename)
        self.allMovies[self.uniqueId] = MovieAttributes()
        self.allMovies[self.uniqueId].pros = ['any positive note']
        self.allMovies[self.uniqueId].cons = ['why you dont want to continue this watching this movie']
        self.allMovies[self.uniqueId].whatisMissing = ['enter what is missing in the movie']


    def addPros(self, uniqueId, pro):
        self.allMovies[uniqueId].pros.append(pro)

    def addCons(self, uniqueId, con):
        self.allMovies[uniqueId].cons.append(con)

    def addWhatisMissing(self, uniqueId, what):
        self.allMovies[uniqueId].whatisMissing.append(what)



class MovieAttributes:
    def __init__(self):
        self.pros = [],
        self.cons = [],
        self.whatisMissing=[]

MovieMetaList = [
    MovieMetaInfo(2022,"Stellar"),
    MovieMetaInfo(2023,"Jumanji")
]

def initModule():
    print('init module')
    MovieMetaList[0].addPros('2022_Stellar','thriller')
    MovieMetaList[0].addCons('2022_Stellar','violence')
    MovieMetaList[0].addWhatisMissing('2022_Stellar','more science')
    print(MovieMetaList[0].allMovies['2022_Stellar'].pros)
    MovieMetaList[1].addPros('2023_Jumanji','thriller')
    MovieMetaList[1].addCons('2023_Jumanji','ugly animals')
    MovieMetaList[1].addWhatisMissing('2023_Jumanji','more innovation')
def printAllMovies():
    for x in MovieMetaList:
        print('Movie-->'+x.uniqueId)
        print(x.allMovies[x.uniqueId].pros)
        print(x.allMovies[x.uniqueId].cons)
        print(x.allMovies[x.uniqueId].whatisMissing)
if __name__ == "__main__":
    initModule()
    printAllMovies()