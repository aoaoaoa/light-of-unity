/*
 * Light of Unity: shared content for every variant.
 * Add later batches by appending to `entries`. Each variant reads this file only.
 *
 * statement  text from the NSA letter (verbatim)
 * echo       passage from Bahá’í literature, with its source as printed
 * ground     colour of the original card: "sage" | "forest" | "teal"
 */
window.UNITY = {
  question: "How powerful is the light of unity?",
  letter: {
    body: "National Spiritual Assembly of the Bahá’ís of the United States",
    form: "Letter",
    dateLabel: "Juneteenth, 2020",
    date: "2020-06-19",
    year: 2020
  },
  note: "Echoes from Bahá’í literature have been added in italics.",
  entries: [
    {
      id: "humanity-is-one",
      ground: "forest",
      statement: "To create a just society begins with recognition of the fundamental truth that humanity is one. But it is not enough simply to believe this in our hearts."
    },
    {
      id: "moral-imperative",
      ground: "forest",
      statement: "It creates the moral imperative to act, and to view all aspects of our personal, social, and institutional lives through the lens of justice.",
      echo: {
        text: "Be anxiously concerned with the needs of the age ye live in, and centre your deliberations on its exigencies and requirements. We can well perceive how the whole human race is encompassed with great, with incalculable afflictions. We see it languishing on its bed of sickness, sore-tried and disillusioned.",
        author: "Bahá’u’lláh",
        work: "The Tabernacle of Unity",
        year: 1882
      }
    },
    {
      id: "reordering",
      ground: "forest",
      statement: "It implies a reordering of our society more profound than anything we have yet achieved. And it requires the participation of Americans of every race and background, for it is only through such inclusive participation that new moral and social directions can emerge.",
      echo: {
        text: "…find those souls longing to shed the lethargy imposed on them by society and work alongside one another in their neighbourhoods and villages to begin a process of collective transformation. If the friends persist in their efforts to learn the ways and methods of community building in small settings in this way, the long-cherished goal of universal participation in the affairs of the Faith will, we are certain, move by several orders of magnitude within grasp.",
        author: "The Universal House of Justice",
        work: "Riḍván 2010 message",
        year: 2010
      }
    },
    {
      id: "new-framework",
      ground: "teal",
      statement: "It is one thing to protest against particular forms of injustice. It is a far more profound challenge to create a new framework for justice.",
      echo: {
        text: "The light of men is Justice. Quench it not with the contrary winds of oppression and tyranny. The purpose of justice is the appearance of unity among men. The ocean of divine wisdom surgeth within this exalted word, while the books of the world cannot contain its inner significance.",
        author: "Bahá’u’lláh",
        work: "Words of Paradise",
        in: "Tablets of Bahá’u’lláh",
        year: 1890
      }
    }
  ]
};
