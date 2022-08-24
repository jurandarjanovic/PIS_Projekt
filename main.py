from website import create_app #web je python paket (importam)

app = create_app()

if __name__ == '__main__': #pokrećem aplikaciju
    app.run(debug=True) #ne moram resetirati server, svaka promjena je spremljena live
