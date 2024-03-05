
import pygame # används för att skapa spel och grafiska applikationer
import numpy as np #stöd för matematiska och numeriska operationer


COLOR_BG = (10, 10, 10) # bakgrundsfärg, grå
COLOR_GRID = (40, 40, 40) # Griddfärg, ljusare grå
COLOR_DIE_NEXT = (10, 10, 10) # färgen för celler som dör nästa gen
COLOR_ALIVE_NEXT = (0, 255, 255) # färg för celler som föds nästa gen

class Skapa_mönster:
    def __init__(self, cells, start_row, start_col, text=''):
        self.cells = cells
        self.start_row = start_row
        self.start_col = start_col
        self.text = text

    def create(self):
        if self.text == 'Beehive':
            self.cells[self.start_row][self.start_col+1] = 1
            self.cells[self.start_row][self.start_col+2] = 1
            # self.cells[self.start_row][self.start_col+3] = 1 # Tillägg för mönster
            self.cells[self.start_row+1][self.start_col] = 1
            self.cells[self.start_row+1][self.start_col+3] = 1
            self.cells[self.start_row+2][self.start_col+1] = 1
            self.cells[self.start_row+2][self.start_col+2] = 1
            return self.cells
        if self.text == 'Glider':
            self.cells[self.start_row][self.start_col] = 1
            self.cells[self.start_row][self.start_col+1] = 1
            self.cells[self.start_row][self.start_col+2] = 1
            self.cells[self.start_row+1][self.start_col+2] = 1
            self.cells[self.start_row+1][self.start_col+2] = 1
            self.cells[self.start_row+2][self.start_col+1] = 1
            return self.cells
        if self.text == 'Glider':
            self.cells[self.start_row][self.start_col] = 1
            self.cells[self.start_row][self.start_col+1] = 1
            self.cells[self.start_row][self.start_col+2] = 1
            self.cells[self.start_row+1][self.start_col+2] = 1
            self.cells[self.start_row+1][self.start_col+2] = 1
            self.cells[self.start_row+2][self.start_col+1] = 1
            return self.cells
        if self.text == 'Gosper glider gun':
            self.cells[self.start_row+1][self.start_col+26] = 1#
            self.cells[self.start_row+2][self.start_col+24] = 1
            self.cells[self.start_row+2][self.start_col+26] = 1
            self.cells[self.start_row+3][self.start_col+14] = 1#
            self.cells[self.start_row+3][self.start_col+15] = 1
            self.cells[self.start_row+3][self.start_col+22] = 1
            self.cells[self.start_row+3][self.start_col+23] = 1
            self.cells[self.start_row+3][self.start_col+36] = 1#
            self.cells[self.start_row+3][self.start_col+37] = 1
            self.cells[self.start_row+4][self.start_col+13] = 1
            self.cells[self.start_row+4][self.start_col+17] = 1
            self.cells[self.start_row+4][self.start_col+22] = 1
            self.cells[self.start_row+4][self.start_col+23] = 1
            self.cells[self.start_row+4][self.start_col+36] = 1
            self.cells[self.start_row+4][self.start_col+37] = 1
            self.cells[self.start_row+5][self.start_col+2] = 1
            self.cells[self.start_row+5][self.start_col+3] = 1
            self.cells[self.start_row+5][self.start_col+12] = 1
            self.cells[self.start_row+5][self.start_col+18] = 1
            self.cells[self.start_row+5][self.start_col+22] = 1
            self.cells[self.start_row+5][self.start_col+23] = 1
            self.cells[self.start_row+6][self.start_col+2] = 1
            self.cells[self.start_row+6][self.start_col+3] = 1
            self.cells[self.start_row+6][self.start_col+12] = 1
            self.cells[self.start_row+6][self.start_col+16] = 1
            self.cells[self.start_row+6][self.start_col+18] = 1
            self.cells[self.start_row+6][self.start_col+19] = 1
            self.cells[self.start_row+6][self.start_col+24] = 1
            self.cells[self.start_row+6][self.start_col+26] = 1
            self.cells[self.start_row+7][self.start_col+12] = 1
            self.cells[self.start_row+7][self.start_col+18] = 1
            self.cells[self.start_row+7][self.start_col+26] = 1
            self.cells[self.start_row+8][self.start_col+13] = 1
            self.cells[self.start_row+8][self.start_col+17] = 1
            self.cells[self.start_row+9][self.start_col+14] = 1
            self.cells[self.start_row+9][self.start_col+15] = 1
            return self.cells


# KnappKlass
class Button:
    def __init__(self, x, y, width, height, text='', color=(0, 150, 0), highlight_color=(0, 200, 0), action=None):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.highlight_color = highlight_color
        self.action = action
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.highlight_color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("arial", 20)
        text_surf = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect()
        text_rect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
        screen.blit(text_surf, text_rect)

#ActionFunktioner (skapa class för detta?)
def button_action_beehive(cells):
    skapa_mönster = Skapa_mönster(cells, 30, 50, 'Beehive')
    cells = skapa_mönster.create()
    return cells

def button_action_glider(cells):
    skapa_mönster = Skapa_mönster(cells, 50, 35, 'Glider')
    cells = skapa_mönster.create()
    return cells

def button_action_Gosper_glider_gun(cells):
    skapa_mönster = Skapa_mönster(cells, 20, 35, 'Gosper glider gun')
    cells = skapa_mönster.create()
    return cells




# Funktion 'update' som tar in skrämen, en matris med celler, storleken på varje
# cell och en flagga som indikerar om en uppdatering ska göras med framsteg
def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros_like(cells) # Skapa en tom matris för uppdaterade celler

    rows, cols = cells.shape # Hämta antalet rader och kolumner i cellmatrisen

    # Loopa genom varje cell i matrisen cells
    for row in range(rows):
        for col in range(cols):
            # Beräkna antalet levande grannar för den aktuella cellen
            alive = 0
            for i in range(max(0, row - 1), min(rows, row + 2)):
                for j in range(max(0, col - 1), min(cols, col + 2)):
                    if (i, j) != (row, col) and cells[i, j] == 1:
                        alive += 1

            # Bestäm färgen för cellen beroende på dess aktuella tillstånd
            color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

            # Om cellen är levande
            if cells[row, col] == 1:
                # Om antalet levande grannar är mindre än 2 eller större än 3
                if alive < 2 or alive > 3:
                    # Om with_progress är True, ändra färgen för att indikera att cellen kommer att dö
                    if with_progress:
                        color = COLOR_DIE_NEXT
                    # Uppdatera cellens tillstånd i den uppdaterade cellmatrisen
                    updated_cells[row, col] = 0
                # Om antalet levande grannar är 2 eller 3
                elif 2 <= alive <= 3:
                    # Uppdatera cellens tillstånd i den uppdaterade cellmatrisen
                    updated_cells[row, col] = 1
                    # Om with_progress är True, ändra färgen för att indikera att cellen kommer att förbli levande
                    if with_progress:
                        color = COLOR_ALIVE_NEXT
            # Om cellen är död
            else:
                # Om antalet levande grannar är exakt 3
                if alive == 3:
                    # Uppdatera cellens tillstånd i den uppdaterade cellmatrisen
                    updated_cells[row, col] = 1
                    # Om with_progress är True, ändra färgen för att indikera att cellen kommer att bli levande
                    if with_progress:
                        color = COLOR_ALIVE_NEXT

            # Rita en rektangel för den aktuella cellen på skärmen med den beräknade färgen
            pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    # Returnera den uppdaterade cellmatrisen
    return updated_cells



def main():
    pygame.init() # Initierar Pygame-modulen
    screen = pygame.display.set_mode((1200, 600)) # Skapar ett fönster med bredd 800 och höjd 600 pixlar
    cells = np.zeros((55, 100)) # Skapar en matris med dim 80x100 som representerar spelplanen, där alla celler initialt är döda
    
    # Knappinställningar
    button_Skapa_glider = Button(1000, 1, 200, 50, text="Skapa en glider!", color=(0, 150, 0), highlight_color=(0, 200, 0), action=button_action_glider)
    button_Skapa_beehive = Button(1000, 52, 200, 50, text="Skapa en beehive!", color=(0, 150, 0), highlight_color=(0, 200, 0), action=button_action_beehive)
    button_Skapa_Gosper_glider_gun = Button(1000, 103, 200, 50, text="Skapa en Gosper glider gun!", color=(0, 150, 0), highlight_color=(0, 200, 0), action=button_action_Gosper_glider_gun)
    button_Skapa_space = Button(0, 549, 499, 50, text="Space = Start/Stop", color=(0, 150, 0), highlight_color=(0, 200, 0), action=None)
    button_Skapa_enter = Button(500, 549, 499, 50, text="Enter = Reset", color=(0, 150, 0), highlight_color=(0, 200, 0), action=None)

    screen.fill(COLOR_GRID) # Fyller skärmen med färgen som definierat för rutnätet
    update(screen, cells, 10) # Uppdaterar skärmen med den initiala cellinformationen och storleken på varje cell
    pygame.display.flip() # Uppdaterar skärmen

    running = True
    clock = pygame.time.Clock() # Skapa en klocka för att reglera framerate
    FPS = 10 # Frames per second

    while True: # oändlig loop
        clock.tick(FPS)
        for event in pygame.event.get(): #Loopar alla händelser som inträffar
            if event.type == pygame.QUIT: #Om händelsen är att användaren stänger fönstret, avslutas spelet
                pygame.quit()
                return
           
            elif event.type == pygame.KEYDOWN: # Om händelsen är att en tangent trycktes ned:
                if event.key == pygame.K_SPACE: # Om "tangent" var mellanslag, bryter "running"-flaggan till sitt motsatta värde
                    running = not running #
                    update(screen, cells, 10) # Uppdaterar skärmen med den nya informationen
                    pygame.display.update() # uppdatera skärmen
                if event.key == pygame.K_RETURN: # Restartar matrisen
                    cells = np.zeros((55, 100))
                    update(screen, cells, 10)
                    pygame.display.update() # uppdatera skärmen

                    


            elif pygame.mouse.get_pressed()[0]: # Om vänster musknapp trycks ned
                pos = pygame.mouse.get_pos() # Hämta musens position
                # Kontrollera att musens position är inom gränserna för cellmatrisen
                if 0 <= pos [0] < 1000 and 0 <= pos[1] < 550:
                    cells[pos[1] // 10, pos[0] // 10] = 1 # Uppdatera motsvarande cell till levande
                    update(screen, cells , 10) # Uppdatera skärmen med nya celltillstånd
                    pygame.display.update() # Uppdatera displayen
                else:
                    if button_Skapa_beehive.x <= pos[0] <= button_Skapa_beehive.x + button_Skapa_beehive.width and \
                        button_Skapa_beehive.y <= pos[1] <= button_Skapa_beehive.y + button_Skapa_beehive.height:
                        cells = button_Skapa_beehive.action(cells) # Anropa knappens åtgärd
                        update(screen, cells, 10) # Uppdatera skärmen med den nya informationen
                        pygame.display.update() # Uppdatera skärmen

                        # Behövs för att knappen ska funka
                    if button_Skapa_glider.x <= pos[0] <= button_Skapa_glider.x + button_Skapa_glider.width and \
                        button_Skapa_glider.y <= pos[1] <= button_Skapa_glider.y + button_Skapa_glider.height:
                        cells = button_Skapa_glider.action(cells) # Anropa knappens åtgärd
                        update(screen, cells, 10) # Uppdatera skärmen med den nya informationen
                        pygame.display.update() # Uppdatera skärmen

                    if button_Skapa_Gosper_glider_gun.x <= pos[0] <= button_Skapa_Gosper_glider_gun.x + button_Skapa_Gosper_glider_gun.width and \
                        button_Skapa_Gosper_glider_gun.y <= pos[1] <= button_Skapa_Gosper_glider_gun.y + button_Skapa_Gosper_glider_gun.height:
                        cells = button_Skapa_Gosper_glider_gun.action(cells) # Anropa knappens åtgärd
                        update(screen, cells, 10) # Uppdatera skärmen med den nya informationen
                        pygame.display.update() # Uppdatera skärmen

            elif pygame.mouse.get_pressed()[2]: # Om höger musknapp trycks ned
                pos = pygame.mouse.get_pos() # Hämta musens position
                # Kontrollera att musens position är inom gränserna för cellmatrisen
                if 0 <= pos [0] < 1000 and 0 <= pos[1] < 550: 
                    cells[pos[1] // 10, pos[0] // 10] = 0 # Uppdatera motsvarande cell till död
                    update(screen, cells , 10) # Uppdatera skärmen med nya celltillstånd
                    pygame.display.update() # Uppdatera displaye

        screen.fill(COLOR_GRID) # Fyller skärmen med färgen för rutnätet
                    # Rita knappen på skärmen
        button_Skapa_beehive.draw(screen) 
        button_Skapa_glider.draw(screen)
        button_Skapa_Gosper_glider_gun.draw(screen)
        button_Skapa_space.draw(screen)
        button_Skapa_enter.draw(screen)
        


        if running: # "Om spelet körs"
            cells = update(screen, cells , 10, with_progress=True) # uppdaterar cellerna med "progressindikator"
            pygame.display.update() # uppdaterar skärmen med den nya informationen


if __name__ == '__main__':  # kör main()-funktionen om skriptet körs som huvudprogram
    main()
