import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./utils/schema.js",
  out: "./drizzle",
  dbCredentials: {
    url: "postgresql://accounts:npg_k9LnDEfjd3bl@ep-snowy-feather-a8hh6ymv-pooler.eastus2.azure.neon.tech/ai-interview-mocker?sslmode=require",
  },
});
