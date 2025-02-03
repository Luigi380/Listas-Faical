personagens = {
    "zangief": 
        {
            "forca": 100,         
            "vida": 150,         
            "velocidade": 0,         
            "magia": 0, 
        },     
    "ken": 
        {
            "forca": 50,         
            "vida": 100,         
            "velocidade": 50,         
            "magia": 50
        },     
    "ryu": 
        {
            "forca": 75,         
            "vida": 100,         
            "velocidade": 50,         
            "magia": 25
        },     
    "chun-li": 
        {
            "forca": 25,         
            "vida": 75,         
            "velocidade": 125,         
            "magia": 50
        }
} 

lutas = [
    {"p1": "ryu", "p2": "ryu", "venceu": "p1"},     
    {"p1": "ken", "p2": "zangief", "venceu": "p2"},     
    {"p1": "ken", "p2": "chun-li", "venceu": "p1"},     
    {"p1": "ken", "p2": "ken", "venceu": "p2"},     
    {"p1": "zangief", "p2": "zangief", "venceu": "p2"},     
    {"p1": "ryu", "p2": "chun-li", "venceu": "p2"},     
    {"p1": "chun-li", "p2": "chun-li", "venceu": "p1"}, 
]

def somaEstatisticas(personagens):
    for i in personagens:
        pass