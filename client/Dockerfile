# Use Node.js 18 (Alpine version for a smaller image)
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install all Vue dependencies
# If package-lock.json exists, install exact versions
RUN npm install

# Install Vite if it's not already in node_modules
RUN npm list vite || npm install --save-dev vite @vitejs/plugin-vue

# Copy all Vue CLI project files into the container
COPY . .

# Expose Vite's default development server port
EXPOSE 5173

# Start the Vite development server
CMD ["npm", "run", "dev"]
