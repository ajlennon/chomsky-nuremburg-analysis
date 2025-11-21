"""
Chomsky Claims Extractor

Extracts and structures all claims from Chomsky's essay
"If the Nuremberg Laws were Applied..."

Copyright (C) 2025
License: GPL-3.0-or-later
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Claim:
    """Represents a specific claim to be verified"""

    id: str
    category: str
    claim_text: str
    context: str
    keywords: List[str]
    expected_documents: List[str]
    verification_notes: Optional[str] = None


class ChomskyClaimsExtractor:
    """Extracts and structures claims from Chomsky's essay"""

    def __init__(self):
        self.claims: List[Claim] = []
        self._extract_claims()

    def _extract_claims(self):
        """Extract all claims from Chomsky's essay"""

        # Category 1: General Yamashita Case (Tokyo Trials)
        self.claims.append(
            Claim(
                id="yamashita_001",
                category="Tokyo Trials - General Yamashita",
                claim_text="General Yamashita was hanged on the grounds that troops in the Philippines, which were technically under his command (though it was so late in the war that he had no contact with them), had carried out atrocities",
                context="Chomsky argues that Yamashita was hanged for atrocities committed by troops he had no contact with",
                keywords=["Yamashita", "Philippines", "atrocities", "command", "hanged", "Tokyo"],
                expected_documents=[
                    "Tokyo Trial transcripts",
                    "Yamashita judgment",
                    "Tokyo Tribunal documents",
                ],
            )
        )

        # Category 2: Justice Radhabinod Pal's Dissent
        self.claims.append(
            Claim(
                id="pal_001",
                category="Tokyo Trials - Justice Pal Dissent",
                claim_text="Radhabinod Pal was the one authentic, independent Asian justice at the Tokyo tribunal, and also the one person in the court who had any background in international law",
                context="Chomsky describes Pal's qualifications and independence",
                keywords=[
                    "Radhabinod Pal",
                    "Indian",
                    "justice",
                    "international law",
                    "Tokyo tribunal",
                ],
                expected_documents=["Pal dissent", "Tokyo Tribunal judges", "Pal biography"],
            )
        )

        self.claims.append(
            Claim(
                id="pal_002",
                category="Tokyo Trials - Justice Pal Dissent",
                claim_text="Pal dissented from the whole judgment, dissented from the whole thing. He wrote a very interesting and important dissent, seven hundred pages",
                context="Pal's comprehensive dissent from the Tokyo Tribunal judgment",
                keywords=["Pal", "dissent", "seven hundred pages", "judgment"],
                expected_documents=["Pal dissent document", "Tokyo Tribunal judgment"],
            )
        )

        self.claims.append(
            Claim(
                id="pal_003",
                category="Tokyo Trials - Justice Pal Dissent",
                claim_text="Pal's dissent can be found in the Harvard Law Library",
                context="Location of Pal's dissent document",
                keywords=["Pal", "dissent", "Harvard Law Library"],
                expected_documents=["Harvard Law Library catalog", "Pal dissent location"],
            )
        )

        self.claims.append(
            Claim(
                id="pal_004",
                category="Tokyo Trials - Justice Pal Dissent",
                claim_text="Pal ends up by saying something like this: if there is any crime in the Pacific theater that compares with the crimes of the Nazis, for which they're being hanged at Nuremberg, it was the dropping of the two atom bombs",
                context="Pal's comparison of atom bombs to Nazi crimes",
                keywords=[
                    "Pal",
                    "atom bomb",
                    "Hiroshima",
                    "Nagasaki",
                    "Nazi crimes",
                    "Pacific theater",
                ],
                expected_documents=["Pal dissent", "atom bomb discussion"],
            )
        )

        self.claims.append(
            Claim(
                id="pal_005",
                category="Tokyo Trials - Justice Pal Dissent",
                claim_text="Pal says nothing of that sort can be attributed to the present accused",
                context="Pal's statement that atom bomb crimes cannot be attributed to the accused",
                keywords=["Pal", "atom bomb", "accused", "attributed"],
                expected_documents=["Pal dissent"],
            )
        )

        # Category 3: Operational Criterion for War Crimes
        self.claims.append(
            Claim(
                id="criterion_001",
                category="Nuremberg Principles - Operational Criterion",
                claim_text="If the enemy had done it and couldn't show that we had done it, then it was a war crime. There was a criterion. Kind of like an operational criterion",
                context="Chomsky's description of how war crimes were determined at Nuremberg/Tokyo",
                keywords=["war crime", "criterion", "operational criterion", "enemy", "Nuremberg"],
                expected_documents=[
                    "Nuremberg principles",
                    "Telford Taylor",
                    "Nuremberg and Vietnam",
                ],
            )
        )

        self.claims.append(
            Claim(
                id="criterion_002",
                category="Nuremberg Principles - Operational Criterion",
                claim_text="Bombing of urban concentrations was not considered a war crime because we had done more of it than the Germans and the Japanese",
                context="Why bombing cities wasn't considered a war crime",
                keywords=["bombing", "urban concentrations", "war crime", "Dresden", "Tokyo"],
                expected_documents=["Nuremberg trial documents", "bombing discussions"],
            )
        )

        self.claims.append(
            Claim(
                id="criterion_003",
                category="Nuremberg Principles - Operational Criterion",
                claim_text="You want to turn Tokyo into rubble? So much rubble you can't even drop an atom bomb there because nobody will see anything if you do, which is the real reason they didn't bomb Tokyo",
                context="Why Tokyo wasn't atom bombed",
                keywords=["Tokyo", "rubble", "atom bomb", "bombing"],
                expected_documents=["atom bomb decision documents"],
            )
        )

        self.claims.append(
            Claim(
                id="criterion_004",
                category="Nuremberg Principles - Operational Criterion",
                claim_text="Bombing Dresden is not a war crime. We did it",
                context="Dresden bombing not considered a war crime",
                keywords=["Dresden", "bombing", "war crime"],
                expected_documents=["Dresden bombing", "Nuremberg documents"],
            )
        )

        # Category 4: Admiral Gernetz/Nimitz Case
        self.claims.append(
            Claim(
                id="gernetz_001",
                category="Nuremberg Trials - Admiral Gernetz Case",
                claim_text="German Admiral Gernetz - when he was brought to trial (he was a submarine commander or something) for sinking merchant vessels or whatever he did - he called as a defense witness American Admiral Nimitz who testified that the U.S. had done pretty much the same thing, so he was off, he didn't get tried",
                context="Gernetz case where Nimitz testified that US did similar things",
                keywords=["Gernetz", "Nimitz", "submarine", "merchant vessels", "defense witness"],
                expected_documents=["Gernetz trial", "Nimitz testimony", "submarine warfare"],
            )
        )

        # Category 5: Telford Taylor and Nuremberg Principles
        self.claims.append(
            Claim(
                id="taylor_001",
                category="Nuremberg Principles - Telford Taylor",
                claim_text="The chief prosecutor at Nuremberg was Telford Taylor. You know, a decent man. He wrote a book called Nuremberg and Vietnam",
                context="Telford Taylor's role and his book",
                keywords=[
                    "Telford Taylor",
                    "chief prosecutor",
                    "Nuremberg",
                    "Nuremberg and Vietnam",
                ],
                expected_documents=["Telford Taylor biography", "Nuremberg and Vietnam book"],
            )
        )

        self.claims.append(
            Claim(
                id="taylor_002",
                category="Nuremberg Principles - Telford Taylor",
                claim_text="In Nuremberg and Vietnam, Taylor tries to consider whether there are crimes in Vietnam that fall under the Nuremberg principles. Predictably, he says not",
                context="Taylor's conclusion about Vietnam and Nuremberg principles",
                keywords=[
                    "Telford Taylor",
                    "Nuremberg and Vietnam",
                    "Vietnam",
                    "Nuremberg principles",
                ],
                expected_documents=["Nuremberg and Vietnam book"],
            )
        )

        self.claims.append(
            Claim(
                id="taylor_003",
                category="Nuremberg Principles - Telford Taylor",
                claim_text="Taylor spells out the Nuremberg principles. They're just the way I said. In fact, I'm taking it from him, but he doesn't regard that as a criticism. He says, well, that's the way we did it, and should have done it that way",
                context="Taylor's explanation of Nuremberg principles matching Chomsky's description",
                keywords=["Telford Taylor", "Nuremberg principles", "operational criterion"],
                expected_documents=["Nuremberg and Vietnam book", "Yale Law Journal article"],
            )
        )

        self.claims.append(
            Claim(
                id="taylor_004",
                category="Nuremberg Principles - Telford Taylor",
                claim_text="There's an article on this in The Yale Law Journal [Review Symposium: War Crimes, the Rule of Force in International Affairs, The Yale Law Journal, Vol. 80, #7, June 1971] which is reprinted in a book [Chapter 3 of Chomsky's For Reasons of State (Pantheon, 1973)]",
                context="Reference to Yale Law Journal article",
                keywords=["Yale Law Journal", "War Crimes", "Rule of Force", "June 1971"],
                expected_documents=["Yale Law Journal", "For Reasons of State"],
            )
        )

        # Category 6: Ex Post Facto Nature of Nuremberg
        self.claims.append(
            Claim(
                id="expost_001",
                category="Nuremberg Principles - Ex Post Facto",
                claim_text="The Nuremberg principles were ex post facto. These were determined to be crimes by the victors after they had won",
                context="Nuremberg principles were retroactive",
                keywords=["ex post facto", "victors", "crimes", "Nuremberg principles"],
                expected_documents=["Nuremberg principles", "trial documents"],
            )
        )

        # Category 7: Tokyo Tribunal Assessment
        self.claims.append(
            Claim(
                id="tokyo_001",
                category="Tokyo Trials - General Assessment",
                claim_text="The Tokyo tribunal was in many ways farcical. The people condemned at Tokyo had done things for which plenty of people on the other side could be condemned",
                context="Chomsky's assessment of Tokyo Tribunal as farcical",
                keywords=["Tokyo tribunal", "farcical", "condemned"],
                expected_documents=["Tokyo Tribunal documents", "Tokyo Trial transcripts"],
            )
        )

        self.claims.append(
            Claim(
                id="tokyo_002",
                category="Tokyo Trials - General Assessment",
                claim_text="Many of their worst atrocities the U.S. didn't care about. Like some of the worst atrocities of the Japanese were in the late '30s, but the U.S. didn't especially care about that. What the U.S. cared about was that Japan was moving to close off the China market",
                context="US priorities regarding Japanese atrocities",
                keywords=["Japanese atrocities", "1930s", "China market", "Nanking"],
                expected_documents=["Tokyo Trial documents", "US-Japan relations"],
            )
        )

        self.claims.append(
            Claim(
                id="tokyo_003",
                category="Tokyo Trials - General Assessment",
                claim_text="The slaughter of a couple of hundred thousand people or whatever they did in Nanking. That's not a big deal",
                context="US attitude toward Nanking massacre",
                keywords=["Nanking", "massacre", "atrocities"],
                expected_documents=["Nanking massacre", "Tokyo Trial documents"],
            )
        )

        # Category 8: American Presidents Claims (for context, but not primary verification focus)
        # Note: These require external historical sources, not just Nuremberg documents
        self.claims.append(
            Claim(
                id="presidents_001",
                category="American Presidents - Context",
                claim_text="If the Nuremberg laws were applied, then every post-war American president would have been hanged",
                context="Chomsky's main thesis about American presidents",
                keywords=["American presidents", "Nuremberg laws", "hanged"],
                expected_documents=["Nuremberg principles", "war crimes definitions"],
                verification_notes="This requires comparing presidential actions to Nuremberg principles, not just verifying within Nuremberg documents",
            )
        )

    def get_all_claims(self) -> List[Claim]:
        """Get all extracted claims"""
        return self.claims

    def get_claims_by_category(self, category: str) -> List[Claim]:
        """Get claims filtered by category"""
        return [c for c in self.claims if c.category == category]

    def get_claim_by_id(self, claim_id: str) -> Optional[Claim]:
        """Get a specific claim by ID"""
        for claim in self.claims:
            if claim.id == claim_id:
                return claim
        return None
