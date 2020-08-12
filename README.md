# izkor topic modeling

אתר הפרויקט - https://naamar30.wixsite.com/izkor-topic-modeling

מטרת הפרויקט:

בפרויקט זה נחקור את הנושאים המרכזיים המצוינים בכתבי היזכור של משפחות הנופלים.

נחקור את הנושאים המדוברים לאורך השנים, על פי עשורים שונים. 

נחקור את הנושאים השונים על פי עשורים לפי מגדר ונראה את אחוז הנושא אצל נשים וגברים.
פרויקט זה בוצע במסגרת קורס "מדעי הרוח הדיגיטליים" באוניברסיטת בן גוריון, בשנת 2020.

קישור לאתר הקורס - https://moodle2.bgu.ac.il/moodle/course/view.php?id=31196

​

הכנת ה metadata:​

קיבלנו פרויקט open refine המכיל את מאגר הידע של אתר "היזכור". במאגר ישנן 21,435 רשומות. ברשומות אלו ישנם פרטים על כל נופל כמו שם, שמות ההורים, מקום הקבורה, מספר הקבר וכו'...

כמו כן לכל נופל יש את סיפור חייו אשר משפחתו כתבה עליו. בחרנו להתמקד בסיפורים אלה במחקר שלנו.

בשלב הראשון חילצנו מתוך פרויקט ה-open refine את סיפור חייו של כל חלל, השנה שבה נהרג ומגדרו, את סיפורי החיים שמרנו בתור קבצי טקסט והם היוו את הקורפוס שלנו.

בשלב השני כתבנו תכנית ב-Python על מנת לחלק את הטקסטים לפי עשורים ולפי מגדר, זאת בכדי שנוכל להפעיל כלי ניתוח מתאימים עבור הממצאים של האלגוריתם topic-modeling.



עיבוד המידע:

המטרה הראשונה שלנו הייתה לבדוק מהם הנושאים העיקריים המוזכרים בטקסטים של סיפורי החיים של החללים. לשם כך השתמשנו בשני כלים מרכזיים:

הראשון הנו BGU NLP - lemLDA. (מקור: https://www.cs.bgu.ac.il/~elhadad/nlpproj/LDAforHebrew.html)

כלי זה הנו חבילת Topic Modeling המממשת Latent Dirichlet Allocation) LDA) בעברית. כמו כן, חבילה זו מכילה גם מתייג חלקי דיבר (תוכנית המקבלת טקסט בעברית כקלט וכפלט מחזירה את הטקסט מתויג), כיוון שהשפה העברית נחשבת קשה יחסית וקיימות הטיות רבות לכל מילה בשפה, על המתייג לבצע ניתוח מורפולוגי תוך כדי התיוג.

הרצנו על הטקסטים את כל שלבי מתייג חלקי הדיבר.

הכלי השני אשר השתמשנו בו הנו חבילת MALLET. (מקור: https://programminghistorian.org/en/lessons/topic-modeling-and-mallet#the-composition-of-your-documents)

חבילה זו מבוססת java ומשמשת לעיבוד שפה טבעית סטטיסטית, סיווג מסמכים, חילוץ מידע ועוד. כמו כן בחבילה זו קיים כלי של topic modeling אותו הרצנו על הקורפוס שלנו.

הרצנו topic modeling עם מספר נושאים שונה (10,20,30) ובכל פעם ניתחנו את התוצאות בהתאם. ראינו שכאשר אנו מחלקות ל10 נושאים בלבד, מאוד קשה לתת תיאור חד משמעי עבור כל נושא. כאשר הרצנו 30 נושאים הרגשנו שיש הרבה נושאים שחוזרים על עצמם ומציגים את אותו הדבר.

לכן בחרנו ב20 נושאים כמספר הנושאים שייצג בצורה הטובה ביותר את הנושאים המרכזיים המדוברים בטקסטים אלו.

לאחר בחינת מספר הנושאים ניגשנו לבחון את חלוקת הנושאים לאורך השנים, ונפח המגדר בכל נושא. את המסקנות נפרט בניתוח הנתונים מטה.

​​

הצגת המידע:

בחרנו לייצג את 20 הנושאים המרכזיים עבור כל הטקסטים בword clouds. לכל נושא ישנה הצגה של המילים המרכיבות את הנושא, על פי הנפח שהמילה תופסת מתוך המילים באותו הנושא.

בחרנו להציג את שינוי נפח הנושאים במהלך השנים על ידי SteamGraph אשר ניתן לראות באתר בלשונית "הנושאים לאורך השנים", ניתן לראות כיצד באים לידי ביטוי נושאים ספציפיים בשנים מסוימות לעומת שנים אחרות, למשל נושא מלחמת העולם השנייה מאוד מדובר סביב העשורים 1940-1950.

בנוסף בחרנו להציג לכל עשור גרף שמראה עבור כל topic את האחוזים בין הטקסטים ששייכים לאותו הנושא על פי מגדר. ניתן לראות את הגרפים באתר בלשונית "נושאים לפי מגדר לאורך השנים".

​

ניתוח הנתונים:

כאשר אנו פונות לנתח את הנתונים שהתקבלו אנחנו מנסות לחקור את הנושאים השונים. ניתן לראות שרוב המילים וכמו כן הנושאים הם סביב צבא, פעילויות צבאיות, תפקידים צבאיים, מילות מפתח של צבא כגון פלוגה, מפקד, פעולה...

כמו כן בא לידי ביטוי נושא המשפחה שגם יכולנו לצפות שייקח חלק לא קטן בסיפור חייהם של הנופלים.

עוד נושאים שבאו לידי ביטוי הנם תחביבים כמו שירה, ספורט, וגם לימודים ודת.

ניתוח הנושאים לאורך השנים הוביל אותנו לכמה מסקנות כגון:

סביב שנות מלחמות ישראל ניתן לראות כי ישנם יותר טקסטים וכמו כן הנושאים שקשורים לצבא באים יותר לידי ביטוי בשנים אלו לעומת שנים אחרות.

סביב השנים 1940-1950 ניתן לראות כי נושא מלחמת העולם השנייה מופיע בצורה משמעותית ולא מופיע בשאר השנים כמעט בכלל.

סביב הקמת המדינה ניתן להבחין כי נושא שמופיעות בו המילים יהודי, ערבי, בריטי, עלייה הנו בולט ובעל נפח, בהתאם לתזמון של הקמת המדינה. נושא זה כמעט לא מופיע בשנים שאחרי.

ניתוח הנושאים לפי מגדר:

כאשר אנו רוצות לבחון את הנושאים לפי מגדר אנחנו נתקלות בקושי. ישנם נושאים שיש הבדלים משמעותיים בין אחוז הנשים לגברים וזה משתנה לאורך העשורים השונים וגם בא לידי ביטוי בנושאים שונים בכל כמה עשורים, אך לצערנו אנו מרגישות שנושאים אלו שניתן להפיק מהם מידע רלוונטי לגבי השוני במגדר כלליים מדי ומתמקדים בעיקר במילים צבאיות ולכן לא ניתן להסיק מסקנות מעניינות ממידע זה. דבר שכן ניתן להבחין בו והוא לא מפתיע כל כך זה שבשנים הראשונות 1900-1920 אין כמעט טקסטים ששייכים לנשים, כלומר פחות נשים שנפלו.

בנוסף כאשר התחלנו את פרויקט זה אחת הציפיות שלנו הייתה לראות את נושא המאכלים בא לידי ביטוי בצורה משמעותית בטקסטים, חשבנו שנושא זה יהווה חלק בלתי נפרד מטקסט היזכור עבור הנופלים. גילינו כי זה לא משמעותי כמו שהנחנו. לא ראינו אפילו מילה אחת שקשורה לנושא זה בניתוח שביצענו. זה נכון גם כאשר הרחבנו את מספר הנושאים ל30 נושאים וגם אז לא ניתן היה לראות מילים מנושא זה.
