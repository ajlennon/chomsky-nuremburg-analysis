# Tokyo Trials Analysis - Initial Findings

**Date:** November 21, 2025  
**Status:** Analysis Started

## Overview

We have begun analyzing Chomsky's Tokyo Trials claims using available online archives. This document summarizes initial findings and next steps.

## Claims to Analyze

We identified **9 Tokyo Trials claims** from Chomsky's essay:

1. **General Yamashita Case** (1 claim)
   - Yamashita was hanged for atrocities by troops he had no contact with

2. **Justice Pal Dissent** (5 claims)
   - Pal was the authentic, independent Asian justice
   - Pal wrote a 700-page dissent
   - Pal's dissent compares atom bombs to Nazi crimes
   - Pal's dissent location (Harvard Law Library)

3. **Tokyo Tribunal Assessment** (3 claims)
   - Tribunal was "farcical"
   - US didn't care about 1930s Japanese atrocities
   - Nanking massacre attitude

## Archives Explored

### 1. Tokyo Trial Database (tokyotrial.cn)
- **Status:** Accessible (may require subscription for full access)
- **Findings:**
  - Found Pal's profile page confirming he was the only judge who found all defendants not guilty
  - Found 4 books/research materials about Pal's dissent:
    - "帕尔博士的日本无罪论" (Pal's Theory of Japanese Innocence)
    - "帕尔法官——东京审判批判和绝对和平主义" (Judge Pal - Tokyo Trial Criticism and Absolute Pacifism)
    - "帕尔——印度·民族主义和东京审判" (Pal - Indian Nationalism and Tokyo Trials)
    - "远东国际军事法庭: 法官帕尔的异议判决书" (IMTFE: Judge Pal's Dissenting Judgment) ⭐ **KEY FINDING**
  - Found 16 trial transcript documents from 1946
  - Database has court records, evidence, and research materials

### 2. University of Wisconsin-Madison Libraries
- **Status:** Subscription required
- **Note:** Full-text documents including transcripts and exhibits

### 3. Japan Center for Asian Historical Records (JACAR)
- **Status:** Not yet explored
- **Note:** Complete digital transcripts of court proceedings

### 4. Hoover Institution Library & Archives
- **Status:** Not yet explored
- **Note:** Stanford University's IMTFE records

## Initial Findings

### Pal's Dissent
- **Confirmed:** Pal was indeed the only judge who found all defendants not guilty (from Pal's profile page)
- **Found:** Reference to Pal's dissenting judgment book in Tokyo Trial Database
- **Next Steps:** 
  - Access the full text of Pal's dissent document
  - Verify Chomsky's claim about 700 pages
  - Verify Chomsky's claim about atom bomb comparison

### Yamashita Case
- **Note:** Yamashita was tried separately by a US military commission in the Philippines, NOT at the Tokyo Trials
- **Finding:** No Yamashita documents found in Tokyo Trial Database (expected, as it's a separate trial)
- **Next Steps:**
  - Search for Yamashita trial records separately
  - Verify Chomsky's claim about command responsibility and lack of contact with troops

### Trial Transcripts
- **Found:** 16 transcript documents from 1946 (early days of the trial)
- **Next Steps:**
  - Search transcripts for mentions of Pal, dissent, atom bombs
  - Search for discussions of US attitude toward Japanese atrocities

## Technical Implementation

Created analysis tools:
- `tokyo_scraper.py` - Scraper for Tokyo Trials archives
- `tokyo_main.py` - Main analysis script

**Current Status:** Basic scraping working, found 20 relevant documents

## Next Steps

1. **Access Full Documents:**
   - Obtain access to Tokyo Trial Database full content (may require subscription)
   - Access University of Wisconsin database (subscription)
   - Locate Pal's dissent document (may be in Harvard Law Library as Chomsky stated)

2. **Verify Specific Claims:**
   - Verify Pal's dissent is 700 pages
   - Verify Pal's atom bomb comparison claim
   - Verify Pal's statement that atom bomb crimes cannot be attributed to accused
   - Verify Yamashita case details (separate from Tokyo Trials)

3. **Expand Search:**
   - Search JACAR for additional transcripts
   - Search Hoover Institution archives
   - Search for Yamashita trial records (separate archive)

4. **Create Verification Reports:**
   - Similar to Nuremberg analysis reports
   - Document findings with citations
   - Update main website with Tokyo Trials verification results

## Challenges

1. **Access Restrictions:** Some archives require subscriptions or institutional access
2. **Language:** Some documents are in Chinese/Japanese, may need translation
3. **Yamashita Separate Trial:** Yamashita was not tried at Tokyo Trials, requires separate archive search
4. **Pal's Dissent Location:** Chomsky says it's in Harvard Law Library - may require physical access

## Resources Found

### Pal-Related Documents
1. http://tokyotrial.cn/Book/index/ca13b4bfa05b4525bce7d081d68e82a4 - Pal's Dissenting Judgment (KEY)
2. http://tokyotrial.cn/Book/index/fe3e7efe1e2646288df98976c646cd4d - Pal's Theory of Japanese Innocence
3. http://tokyotrial.cn/Book/index/aef5f4369cd04f55b7d7f650b47ce9b2 - Judge Pal - Tokyo Trial Criticism
4. http://tokyotrial.cn/Book/index/18bcf713495446f28d1dfb12bfdc43f7 - Pal - Indian Nationalism and Tokyo Trials

### Trial Transcripts
- Multiple transcripts from 1946 available at tokyotrial.cn
- Full transcripts may require subscription access

## Conclusion

We have successfully:
- ✅ Identified all Tokyo Trials claims
- ✅ Created analysis tools
- ✅ Found Pal-related documents including reference to his dissenting judgment
- ✅ Found trial transcripts
- ✅ Confirmed Pal was the only judge who found all defendants not guilty

**Next:** Need to access full document content to verify specific claims about Pal's dissent and atom bomb comparison.

