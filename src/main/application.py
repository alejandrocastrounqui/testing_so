from main.domain.banco import Banco
from main.domain.ladron import Ladron
from main.domain.policia import Policia



banco = Banco()

ladron = Ladron()
ladron.objetivo = banco

policia = Policia()
policia.banco = banco

policia.start()
ladron.start()
