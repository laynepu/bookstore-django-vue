import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";

// Export Vite configuration
export default defineConfig({
  // Register Vue plugin to enable Vue Single File Component (SFC) support
  plugins: [vue()],

  // Configure module resolution
  resolve: {
    alias: {
      // Set "@" to refer to the "src" directory for cleaner imports
      "@": path.resolve(__dirname, "src"), 
    },
  },

  // Important: Configure the development server for Docker compatibility
  server: {
    host: "0.0.0.0",  // Allow external access from Docker container
    port: 5173,       // Ensure it matches the Docker port mapping
    strictPort: true, // Prevent port conflicts
    watch: {
      usePolling: true, // Fix file change detection inside Docker containers
    },
  },

  // Set the base URL for the project
  // This is necessary if deploying to a subdirectory (e.g., "https://example.com/LayneBookstore/")
  base: "/LayneBookstore/", 
});
