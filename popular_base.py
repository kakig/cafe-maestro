from main.models import Insumo
import random
import string

for i in range(10):
    Insumo(
        nome="".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(10)
        ),
        descricao="".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(10)
        ),
        unidade_medida="kg",
    ).save()
