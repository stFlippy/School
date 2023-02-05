#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['F', 'M', 'V', 'A']


# список списков приблизителного роста членов вашей семьи
my_family_height = [[my_family[0] ,175],
                    [my_family[1] ,165],
                    [my_family[2] ,181],
                    [my_family[3] ,173]]


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print ("Father's height is about ", my_family_height[0][1] , 'sm')


print ("Family's common height is about",   my_family_height[0][1]+
                                            my_family_height[1][1]+
                                            my_family_height[2][1]+
                                            my_family_height[3][1], 'sm')


# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
