## installing

#### clone repository
```sh
git clone git@github.com:danialsadri/shop_project_front.git
```

#### change directory
```sh
cd shop_project_front
```

#### config docker compose for development
```sh
docker compose -f docker-compose-development.yml up -d --build
```

#### config docker compose for production 
```sh
docker compose -f docker-compose-production.yml up -d --build
```
