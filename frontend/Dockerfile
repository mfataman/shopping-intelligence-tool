# Dockerfile

# Use the official Node.js image as a parent image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Use a serve image to serve the build
FROM serve:latest

COPY --from=0 /app/build /usr/share/nginx/html

# Expose the port on which the app will run
EXPOSE 3000

# Run the app
CMD ["serve", "-s", "-l", "3000", "usr/share/nginx/html"]