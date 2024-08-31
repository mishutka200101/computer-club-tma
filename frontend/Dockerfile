# Stage 1: Build the application
FROM node:18-alpine AS builder

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install

COPY . .
RUN yarn build

# Stage 2: Serve the application with a minimal image
FROM node:18-alpine

WORKDIR /app

COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

CMD ["yarn", "preview", "--host"]

EXPOSE 4173