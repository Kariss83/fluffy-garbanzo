#coding:utf-8
if __name__ == "__main__":
    import sys, os
    import pygame
    from pygame.locals import*
    pygame.init()
 
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    format_img = ".png"
    args = sys.argv[1:]
 
    functions = {}
 
    for arg in args:
 
        if arg == "-h":
            print("""
Arguments (Il faut coller la suite de l'argument là ou un = à été mis):
 
    --format=       Format des images (png par défaut)
    --zoom=         Zoom à appliquer
    --resize=       Redimmensionne l'image a une taille u,w ou uxw
    --autocut       Decoupe automatiquement l'image
    --resave        Réenregistre l'image
    --recursive     Applique recursivement sur tout les sous-dossiers
                """)
            sys.exit(0)
 
        elif arg.startswith("--format="):
            format_img = arg.replace("--format=",".")
 
        elif arg.startswith("--zoom="):
            zoom = arg.replace("--zoom=","")
            if zoom != "0"and not zoom.startswith("-"):
                functions["zoom"] = float(zoom)
 
        elif arg.startswith("--resize="):
            if "x" in arg:
                size = arg.replace("--resize=","").split("x")
                functions["resize"] = [int(x) for x in size]
            elif "," in arg:
                size = arg.replace("--resize=","").split("x")
                functions["resize"] = [int(x) for x in size]
 
        elif arg == "--autocut":
            functions["autocut"] = True
         
        elif arg == "--resave":
            functions["resave"] = True
 
        elif arg == "--recursive":
            functions["recursive"] = True
 
 
 
 
    pygame.display.set_caption("Modification en cours...")
 
    win_size = win_width, win_height = 500,40
    win = pygame.display.set_mode(win_size)
 
    listes_erreurs = []
     
    all_files = [file for file in os.listdir(".") if not os.path.isdir(file) and file.endswith(format_img)]
    all_dirs = ["."]
 
    if "recursive" in functions:
        start_dirs = [file for file in os.listdir(".") if os.path.isdir(file)]
 
        def find_files(directory):
            for file in os.listdir(directory):
                if not os.path.isdir(directory+os.sep+file) and file.endswith(format_img):
                    all_files.append(directory+os.sep+file)
                elif os.path.isdir(directory+os.sep+file):
                    find_files(directory+os.sep+file)
                    all_dirs.append(directory+os.sep+file)
 
 
        for dirs in start_dirs:
            all_dirs.append(dirs)
            find_files(dirs)
             
     
    x = win.get_rect()[2]
    y = win.get_rect()[3]
 
    def up_screen(progression):
        win.fill([40,40,40])
        pygame.draw.rect(win,(0,255,20),(0,0,int(x*progression+1),y))
        pygame.display.update()
     
     
    def apply():
        progression = 0
 
        if functions:
            for image in all_files:
 
                try:
                    i = pygame.image.load(image).convert_alpha()
                     
                    if "zoom" in functions:
                        X = i.get_rect()[2]
                        Y = i.get_rect()[3]
                        z = functions["zoom"]
                        i = pygame.transform.smoothscale(i,[int(X*z),int(Y*z)])
                     
                    if "resize" in functions:
                        i = pygame.transform.smoothscale(i,functions["resize"])
                     
                    if "autocut" in functions:
                        i = i.subsurface(i.get_bounding_rect())
 
                    pygame.image.save(i,image)
                except pygame.error: listes_erreurs.append(image)
                progression += 1./len(all_files)
 
                up_screen(progression)
 
 
    print("\nApplique les modifications sur {} dossiers soit {} images\n".format(len(all_dirs),len(all_files)))
    apply()
 
    if listes_erreurs:
        print("\nLes images suivantes n'ont pas pu être modifiées:\n".format(size))
        for erreur in listes_erreurs:
            print(erreur)