def encaja_domino(ficha_1, ficha_2):
    if ficha_1[0] == ficha_2[0] or ficha_1[1] == ficha_2[0] or ficha_1[0] == ficha_2[1] or ficha_1[1] == ficha_2[1]:
        return True
    return False

        
def main():
    ficha = 3, 4
    
    for x in range(1, 7):
        for y in range(1, 7):
            print('Con la ficha', x, '-', y, '-->', encaja_domino(ficha, (x, y)))
            
    
main()