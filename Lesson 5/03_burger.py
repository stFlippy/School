# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

# TODO здесь ваш код

import my_burger

brgr = ""
print("состав бургера: \n")
brgr = my_burger.half_roll(brgr)
brgr = my_burger.cutlet(brgr)
brgr = my_burger.cucumber(brgr)
brgr = my_burger.tomato(brgr)
brgr = my_burger.mayo(brgr)
brgr = my_burger.chese(brgr)
brgr = my_burger.half_roll(brgr)

print(brgr, "\nбургер готов")
