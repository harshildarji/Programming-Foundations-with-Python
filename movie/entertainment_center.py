import media, movieHTML

avengers = media.Movie('The Avengers',
                     'https://2a867256d194bb3c3c8e994e95aa694e23a8fa55-www.googledrive.com/host/0B9svjAuZEeT4cWFtaHA4bGFfcjA/avengers.jpg',
                     'https://youtu.be/eOrNdBpGMv8')

avengers2 = media.Movie('Avengers: Age of Ultron',
                     'https://2a867256d194bb3c3c8e994e95aa694e23a8fa55-www.googledrive.com/host/0B9svjAuZEeT4cWFtaHA4bGFfcjA/avengers2.jpg',
                     'https://youtu.be/JAUoeqvedMo')

nysm = media.Movie('Now you see me 2',
                   'https://2a867256d194bb3c3c8e994e95aa694e23a8fa55-www.googledrive.com/host/0B9svjAuZEeT4cWFtaHA4bGFfcjA/nysm.jpg',
                   'https://youtu.be/4I8rVcSQbic')

martian = media.Movie('The Martian',
                      'https://2a867256d194bb3c3c8e994e95aa694e23a8fa55-www.googledrive.com/host/0B9svjAuZEeT4cWFtaHA4bGFfcjA/martian.jpg',
                      'https://youtu.be/ej3ioOneTy8')

tmwki = media.Movie('The Man Who Knew Infinity',
                    'https://2a867256d194bb3c3c8e994e95aa694e23a8fa55-www.googledrive.com/host/0B9svjAuZEeT4cWFtaHA4bGFfcjA/tmwki.jpg',
                    'https://youtu.be/oXGm9Vlfx4w')

iceage = media.Movie('Ice Age: Collision Course',
                     'https://2a867256d194bb3c3c8e994e95aa694e23a8fa55-www.googledrive.com/host/0B9svjAuZEeT4cWFtaHA4bGFfcjA/iceage.jpg',
                     'https://youtu.be/s6kGpBTZyr0')

movies = [avengers, avengers2, nysm, martian, tmwki, iceage]
movieHTML.open_movies_page(movies)
