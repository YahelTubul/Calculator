import evaluator
from parser import infix_to_prefix
from tokenize import split_tokenize


def logo():
    logo = """
                                                                                                                                                                                 
                                                                                                                                                                         
                            ,---,                ,--,             ,----..               ,--,                             ,--,                  ___                       
        ,---,             ,--.' |              ,--.'|            /   /   \            ,--.'|                           ,--.'|                ,--.'|_                     
       /_ ./|             |  |  :              |  | :           |   :     :           |  | :                      ,--, |  | :                |  | :,'   ,---.    __  ,-. 
 ,---, |  ' :             :  :  :              :  : '           .   |  ;. /           :  : '                    ,'_ /| :  : '                :  : ' :  '   ,'\ ,' ,'/ /| 
/___/ \.  : |   ,--.--.   :  |  |,--.   ,---.  |  ' |           .   ; /--`   ,--.--.  |  ' |      ,---.    .--. |  | : |  ' |     ,--.--.  .;__,'  /  /   /   |'  | |' | 
 .  \  \ ,' '  /       \  |  :  '   |  /     \ '  | |           ;   | ;     /       \ '  | |     /     \ ,'_ /| :  . | '  | |    /       \ |  |   |  .   ; ,. :|  |   ,' 
  \  ;  `  ,' .--.  .-. | |  |   /' : /    /  ||  | :           |   : |    .--.  .-. ||  | :    /    / ' |  ' | |  . . |  | :   .--.  .-. |:__,'| :  '   | |: :'  :  /   
   \  \    '   \__\/: . . '  :  | | |.    ' / |'  : |__         .   | '___  \__\/: . .'  : |__ .    ' /  |  | ' |  | | '  : |__  \__\/: . .  '  : |__'   | .; :|  | '    
    '  \   |   ," .--.; | |  |  ' | :'   ;   /||  | '.'|        '   ; : .'| ," .--.; ||  | '.'|'   ; :__ :  | : ;  ; | |  | '.'| ," .--.; |  |  | '.'|   :    |;  : |    
     \  ;  ;  /  /  ,.  | |  :  :_:,''   |  / |;  :    ;        '   | '/  :/  /  ,.  |;  :    ;'   | '.'|'  :  `--'   \;  :    ;/  /  ,.  |  ;  :    ;\   \  / |  , ;    
      :  \  \;  :   .'   \|  | ,'    |   :    ||  ,   /         |   :    /;  :   .'   \  ,   / |   :    ::  ,      .-./|  ,   /;  :   .'   \ |  ,   /  `----'   ---'     
       \  ' ;|  ,     .-./`--''       \   \  /  ---`-'           \   \ .' |  ,     .-./---`-'   \   \  /  `--`----'     ---`-' |  ,     .-./  ---`-'                     
        `--`  `--`---'                 `----'                     `---`    `--`---'              `----'                         `--`---'                                 
                                                                                                                                                                              
        """
    print(logo)
    print("=" * 80)
    print("Welcome to the Yahel Advanced Calculator!")
    print("=" * 80)
    print()


def main_calculator():
    logo()
    while True:
        try:
            print("Enter experssion:\n")
            experssion = input("> ").strip()
            tokens = split_tokenize(experssion)
            prfix_tok = infix_to_prefix(tokens)
            result = evaluator.evaluator(prfix_tok)
            print(result)
        except KeyboardInterrupt:
            print("Bye Bye!!!!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main_calculator()
