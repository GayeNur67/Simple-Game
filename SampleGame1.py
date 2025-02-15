import pygame  # type: ignore
import random

# Pygame'i başlat
pygame.init()

# Oyun ekranı ayarları
ekran_genislik = 800
ekran_yukseklik = 600
ekran = pygame.display.set_mode((ekran_genislik, ekran_yukseklik))
pygame.display.set_caption("Top Yakalama Oyunu")

# Renkler
beyaz = (255, 255, 255)
siyah = (0, 0, 0)
kirmizi = (255, 0, 0)
yesil = (0, 255, 0)

# Kutu ayarları
kutu_genislik = 100
kutu_yukseklik = 20
kutu_x = ekran_genislik // 2 - kutu_genislik // 2
kutu_y = ekran_yukseklik - 50
kutu_hiz = 10

# Top ayarları
top_genislik = 20
top_x = random.randint(0, ekran_genislik - top_genislik)
top_y = 0
top_hiz = 5

# Saat
saat = pygame.time.Clock()

# Puan ve kaçırma sayacı
puan = 0
kacirma_hakki = 3  # Oyuncunun 3 kaçırma hakkı var

# Font ayarları
font = pygame.font.Font(pygame.font.match_font('arial'), 30)
game_over_font = pygame.font.Font(pygame.font.match_font('arial'), 100)

# Oyun durumu
calisiyor = True
game_over = False

while calisiyor:
    ekran.fill(beyaz)
    
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            calisiyor = False
    
    if not game_over:
        # Tuş kontrolü
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT] and kutu_x > 0:
            kutu_x -= kutu_hiz
        if tuslar[pygame.K_RIGHT] and kutu_x < ekran_genislik - kutu_genislik:
            kutu_x += kutu_hiz
        
        # Top hareketi
        top_y += top_hiz
        
        # Topun alt sınır kontrolü
        if top_y > ekran_yukseklik:
            kacirma_hakki -= 1
            top_y = 0
            top_x = random.randint(0, ekran_genislik - top_genislik)
            if kacirma_hakki == 0:
                game_over = True
        
        # Çarpışma kontrolü
        if kutu_y < top_y + top_genislik and \
           kutu_x < top_x < kutu_x + kutu_genislik:
            puan += 1
            top_y = 0
            top_x = random.randint(0, ekran_genislik - top_genislik)
        
        # Kutu ve topu çiz
        pygame.draw.rect(ekran, siyah, (kutu_x, kutu_y, kutu_genislik, kutu_yukseklik))
        pygame.draw.ellipse(ekran, siyah, (top_x, top_y, top_genislik, top_genislik))
        
        # Puan ve kaçırma hakkını göster
        puan_metni = font.render(f"Puan: {puan}", True, siyah)
        kacirma_metni = font.render(f"Hak: {kacirma_hakki}", True, siyah)
        ekran.blit(puan_metni, (5, 10))
        ekran.blit(kacirma_metni, (5, 40))
    else:
        # Game Over ekranı
        game_over_metni = game_over_font.render("GAME OVER", True, kirmizi)
        ekran.blit(game_over_metni, 
                   (ekran_genislik // 2 - game_over_metni.get_width() // 2, 
                    ekran_yukseklik // 2 - 100))
        puan_metni = font.render(f"Son Puan: {puan}", True, siyah)
        ekran.blit(puan_metni, 
                   (ekran_genislik // 2 - puan_metni.get_width() // 2, 
                    ekran_yukseklik // 2 + 50))

    pygame.display.update()
    saat.tick(30)

pygame.quit()
