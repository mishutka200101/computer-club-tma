# Используем официальный образ Node.js в качестве базового
FROM node:18-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и yarn.lock
COPY package.json yarn.lock ./

# Устанавливаем зависимости
RUN yarn install

# Копируем остальные файлы проекта
COPY . .

# Собираем приложение
RUN yarn build

# Указываем команду для запуска приложения
CMD ["yarn", "preview", "--host"]

# Открываем порт
EXPOSE 5173