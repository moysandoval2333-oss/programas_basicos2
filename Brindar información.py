opcion = input("Busca un artista, película o serie: ").strip().lower()

match opcion:
    case "the cure":
        print("Banda británica de rock gótico y post-punk. Álbum clave: Disintegration.")
    case "ed sheeran":
        print("Cantautor pop británico. Éxito masivo: Shape of You.")
    case "inception":
        print("Película de Christopher Nolan sobre espionaje en los sueños.")
    case "interstellar":
        print("Película de ciencia ficción sobre un viaje espacial para salvar la humanidad.")
    case "stranger things":
        print("Serie de Netflix con misterios sobrenaturales en los años 80.")
    case _:
        print("Error: Opción inválida. Intenta con otra de la lista.")
