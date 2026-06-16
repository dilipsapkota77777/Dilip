import { z } from "zod";

export const ProspectProfileSchema = z.object({
  name: z.string(),
  title: z.string(),
  company: z.string(),
  industry: z.string(),
  painPoints: z.array(z.string()),
  recentNews: z.array(z.string()),
  personalizationHooks: z.array(z.string()),
});

export const PersonalizationStrategySchema = z.object({
  subjectAngle: z.string(),
  openingHook: z.string(),
  valueProposition: z.string(),
  callToAction: z.string(),
  tone: z.enum(["professional", "conversational", "casual"]),
});

export const ColdEmailSchema = z.object({
  subject: z.string(),
  previewText: z.string(),
  body: z.string(),
});

export const FollowupEmailSchema = z.object({
  day: z.number(),
  strategy: z.string(),
  subject: z.string(),
  body: z.string(),
});

export const FollowupSequenceSchema = z.object({
  initialEmail: ColdEmailSchema,
  followups: z.array(FollowupEmailSchema),
});

export type ProspectProfile = z.infer<typeof ProspectProfileSchema>;
export type PersonalizationStrategy = z.infer<typeof PersonalizationStrategySchema>;
export type ColdEmail = z.infer<typeof ColdEmailSchema>;
export type FollowupEmail = z.infer<typeof FollowupEmailSchema>;
export type FollowupSequence = z.infer<typeof FollowupSequenceSchema>;
