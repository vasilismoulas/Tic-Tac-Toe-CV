import pygame

class SurfaceEditor:
    
    @staticmethod
    def resize_surface(self, surface: pygame.Surface, new_size: tuple) -> pygame.Surface:
        """Resize the given surface to the new size."""
        return pygame.transform.scale(surface, new_size)

    @staticmethod
    def rotate_surface(self, surface: pygame.Surface, angle: float) -> pygame.Surface:
        """Rotate the given surface by the specified angle."""
        return pygame.transform.rotate(surface, angle)

    @staticmethod
    def set_opacity(self, surface: pygame.Surface, alpha: int) -> pygame.Surface:
        """Set the opacity of the given surface (0-255)."""
        surface.set_alpha(alpha)
        return surface
    
    @staticmethod
    def blit_surface(self, target_surface: pygame.Surface, source_surface: pygame.Surface, position: tuple):
        """Blit the source surface onto the target surface at the specified position."""
        target_surface.blit(source_surface, position)

