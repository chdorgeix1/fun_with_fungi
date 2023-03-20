# Restructuring for code:

# Need to implement player1 and player2 lists, hyphae, etc
# Need to implement attack and defense values for the game


# Need menu function, designWorld, createWorld, and beginGame

# Class BaseSprite
class Sprite(pygame.sprite.Sprite):
            def __init__(self, color, height, width, x_loc, y_loc, growing = True, attack_val = 0, defense_val = 0):
                super().__init__()

                self.attack_val = attack_val
                self.defense_val = defense_val
                self.growth_state = growing
                self.color = color
                self.width = width
                self.height = height
                self.image = pygame.Surface([width, height])
                
                self.rect = self.image.get_rect()

                self.rect.x = x_loc
                self.rect.y = y_loc

                pygame.draw.rect(self.image, color,
                                pygame.Rect(0, 0, width, height))
                
            def changeColor(self, new_color):
                self.color = new_color
                pygame.draw.rect(self.image, self.color,
                                    pygame.Rect(0, 0, self.width, self.height))
            
            def naturalGrowth(self, group, growth_count = 0, growthmod = 0, fillrate = 0):
                if self.growth_state == True:
                    growth_list = []
                    for i in [-12, 0, 12]:
                        for j in [-12, 0, 12]:
                            if (self.rect.x + i > 0 and self.rect.x + i < world_dimensions[0]) and (self.rect.y + j > 0 and self.rect.y + j < world_dimensions[1]):
                                growth_list.append((self.rect.x + i, self.rect.y + j))
                    growth_counter = 0
                    for loc in growth_list:
                        example_sprite = sprite_dict[loc]
                        if example_sprite in group and self in group:
                            growth_counter += 1
                        else:
                            if random.random() > 1 - growthmod:
                                if example_sprite in food_sprite_list:
                                    trait_point_dict[self.color] += 1
                                example_sprite.kill()
                                group.add(example_sprite)
                                all_sprites_list.add(example_sprite)
                    if growth_counter >= 9 - growth_count:
                        self.growth_state = False
                else:
                    if random.random() > 1 - fillrate:
                        self.growth_state = True


# Class SlimeHyphae
# Class PoisonHyphae
# Class DurableHyphae

class DurableHyphae(pygame.sprite.Sprite):
            def __init__(self, color, trail, height, width):
                super().__init__()

                self.color = color
                self.trail = trail
                self.width = width
                self.height = height
                self.image = pygame.Surface([width, height])
                
                pygame.draw.rect(self.image,
                                color,
                                pygame.Rect(0, 0, width, height))

                self.rect = self.image.get_rect()    

            def getColors(self):
                return [self.color, self.trail]

            def getX(self):
                return self.rect.x
            
            def getY(self):
                return self.rect.y
            
            def moveRight(self, pixels):
                pygame.draw.rect(sample_surface, self.trail,
                                pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
                self.rect.x += pixels

            def moveLeft(self, pixels):
                pygame.draw.rect(sample_surface, self.trail,
                                pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
                self.rect.x -= pixels

            def moveUp(self, pixels):
                pygame.draw.rect(sample_surface, self.trail,
                                pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
                self.rect.y += pixels

            def moveDown(self, pixels):
                pygame.draw.rect(sample_surface, self.trail,
                                pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
                self.rect.y -= pixels

            def moveUpLeft(self, pixels):
                pygame.draw.rect(sample_surface, self.trail,
                                pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
                self.rect.x -= pixels
                self.rect.y += pixels

            def moveUpRight(self, pixels):
                pygame.draw.rect(sample_surface, self.trail,
                                pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
                self.rect.x += pixels
                self.rect.y += pixels

            def moveDownLeft(self, pixels):
                pygame.draw.rect(sample_surface, self.trail,
                                pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
                self.rect.y -= pixels
                self.rect.x -= pixels

            def moveDownRight(self, pixels):
                pygame.draw.rect(sample_surface, self.trail,
                                pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
                self.rect.y -= pixels
                self.rect.x += pixels
            
            def paintSprites(self,group):
                for example_sprite in all_sprites_list:
                    if example_sprite != playerHyphae or example_sprite != playerHyphae1:
                        if example_sprite.rect[0:2] == self.rect[0:2]:
                            if example_sprite in food_sprite_list:
                                trait_point_dict[self.trail] += 1
                            example_sprite.kill()
                            group.add(example_sprite)
                            defense_cell_list.add(example_sprite)
                            all_sprites_list.add(example_sprite)

# function moveHyphae()
