import pygame
from settings import UI_SETTINGS

def show_value(self, counter_type, lines, x_offset, y_pos,text_size_factor,bg_color,border_color):
    font_size = int(30 * text_size_factor)
    font = pygame.font.Font(None, font_size)

    # Calcular a posição x com base no offset
    x_pos = self.display_surface.get_size()[0] + x_offset  # Verifique o sinal do offset

    box_padding = 20 * text_size_factor
    total_height = box_padding * 2  # Iniciar a altura total com padding

    # Calcular a largura da caixa
    max_width = 0
    for line in lines.values():
        line_width = sum(font.render(item['txt'], False, item['color']).get_width() for item in line)
        max_width = max(max_width, line_width)
        total_height += font.get_height()  # Adiciona a altura da linha

    # Criar o retângulo de fundo
    rect = pygame.Rect(x_pos, y_pos, max_width + box_padding * 2, total_height)
    pygame.draw.rect(self.display_surface,bg_color, rect)

    # Desenhar cada linha
    for i, line in enumerate(lines.values()):
        current_x = x_pos + box_padding  # Iniciar com padding
        for item in line:
            text = item['txt']
            if 'counter' in text:
                index = int(text.replace('counter', ''))
                if index < len(counter_type):
                    text = str(counter_type[index])
            surf = font.render(text, False, item['color'])
            self.display_surface.blit(surf, (current_x, y_pos + box_padding + i * font.get_height()))  # Pular para a linha correta
            current_x += surf.get_width()  # Atualiza a posição x

    # Desenhar a borda da caixa
    pygame.draw.rect(self.display_surface, border_color, rect, 3)