import "dotenv/config";
import { researchProspect } from "./skills/prospectResearch.js";
import { buildPersonalizationStrategy } from "./skills/emailPersonalization.js";
import { generateEmail, generateSimpleEmail } from "./skills/emailGenerator.js";
import { generateFollowupSequence } from "./skills/followupSequences.js";
import type { ColdEmail, ProspectProfile } from "./types.js";

function printEmail(label: string, email: ColdEmail, dayLabel?: string) {
  const header = dayLabel ? `${label} (Day ${dayLabel})` : label;
  console.log(`\n${"=".repeat(60)}`);
  console.log(header);
  console.log("=".repeat(60));
  console.log(`Subject:  ${email.subject}`);
  console.log(`Preview:  ${email.previewText}`);
  console.log("-".repeat(60));
  console.log(email.body);
}

async function runGenerate() {
  if (!process.env.ANTHROPIC_API_KEY) {
    console.error("Error: ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key.");
    process.exit(1);
  }

  // Demo values — replace or wire up to CLI args / your own data source
  const prospect = {
    name: process.env.PROSPECT_NAME ?? "Jane Smith",
    title: process.env.PROSPECT_TITLE ?? "VP of Sales",
    company: process.env.PROSPECT_COMPANY ?? "Acme Corp",
  };
  const sender = {
    name: process.env.SENDER_NAME ?? "Dilip",
    company: process.env.SENDER_COMPANY ?? "YourCo",
    product: process.env.PRODUCT_DESCRIPTION ?? "AI-powered sales tooling",
    benefit: process.env.KEY_BENEFIT ?? "cuts email research time by 80%",
  };
  const fullPipeline = process.env.FULL_PIPELINE === "true";
  const withFollowups = process.env.WITH_FOLLOWUPS === "true";

  console.log(`\nGenerating cold email for ${prospect.name} at ${prospect.company}...`);

  let profile: ProspectProfile | undefined;
  let email: ColdEmail;

  if (fullPipeline) {
    console.log("Step 1/3: Researching prospect...");
    profile = await researchProspect(prospect.name, prospect.title, prospect.company);

    console.log("Step 2/3: Building personalization strategy...");
    const strategy = await buildPersonalizationStrategy(
      profile,
      sender.name,
      sender.company,
      sender.product
    );

    console.log("Step 3/3: Writing email...");
    email = await generateEmail(profile, strategy, sender.name, sender.company, sender.product);
  } else {
    console.log("Generating email...");
    email = await generateSimpleEmail(
      prospect.name,
      prospect.title,
      prospect.company,
      sender.name,
      sender.company,
      sender.product,
      sender.benefit
    );
  }

  printEmail("COLD EMAIL", email);

  if (withFollowups) {
    console.log("\nGenerating follow-up sequence...");
    if (!profile) {
      profile = {
        name: prospect.name,
        title: prospect.title,
        company: prospect.company,
        industry: "unknown",
        painPoints: [sender.benefit],
        recentNews: [],
        personalizationHooks: [sender.benefit],
      };
    }
    const sequence = await generateFollowupSequence(
      profile,
      email,
      sender.name,
      sender.company
    );
    for (const fu of sequence.followups) {
      const fuEmail: ColdEmail = { subject: fu.subject, previewText: "", body: fu.body };
      printEmail(`FOLLOW-UP (strategy: ${fu.strategy})`, fuEmail, String(fu.day));
    }
  }
}

async function runResearch() {
  const name = process.env.PROSPECT_NAME ?? "Jane Smith";
  const title = process.env.PROSPECT_TITLE ?? "VP of Sales";
  const company = process.env.PROSPECT_COMPANY ?? "Acme Corp";

  console.log(`\nResearching ${name}...`);
  const profile = await researchProspect(name, title, company);

  console.log("\n" + "=".repeat(60));
  console.log(`PROSPECT PROFILE: ${profile.name}`);
  console.log("=".repeat(60));
  console.log(`Industry: ${profile.industry}`);
  console.log(`\nPain Points:\n${profile.painPoints.map((p) => `  • ${p}`).join("\n")}`);
  console.log(`\nPersonalization Hooks:\n${profile.personalizationHooks.map((h) => `  • ${h}`).join("\n")}`);
  if (profile.recentNews.length) {
    console.log(`\nRecent News:\n${profile.recentNews.map((n) => `  • ${n}`).join("\n")}`);
  }
}

const command = process.argv[2] ?? "generate";

if (command === "research") {
  runResearch().catch(console.error);
} else {
  runGenerate().catch(console.error);
}
