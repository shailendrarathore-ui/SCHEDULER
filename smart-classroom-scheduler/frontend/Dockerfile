FROM node:22-alpine

WORKDIR /app
COPY package.json vite.config.js postcss.config.js tailwind.config.js ./
COPY src ./src
COPY index.html ./
RUN npm install && npm run build || true

EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
