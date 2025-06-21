import { pgTable, serial, text, varchar, timestamp } from "drizzle-orm/pg-core";

export const MockInterview = pgTable("mockInterview", {
    id: serial("id").primaryKey(),
    jsonMockResp:text('jsonMockResp').notNull(),
    jobPosition:varchar('jobPosition', { length: 255 }).notNull(),
    jobDescr:varchar('jobDescr', { length: 255 }).notNull(),
    jobLocation:varchar('jobLocation', { length: 255 }).notNull(),
    createdBy:varchar('createdBy', { length: 255 }).notNull(),
    createdAt:timestamp('createdAt').notNull().defaultNow(),
    mockInterviewId:varchar('mockInterviewId', { length: 255 }).notNull()
})
