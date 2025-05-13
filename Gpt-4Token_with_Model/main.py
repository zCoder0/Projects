from src.logs.log_config import logging
from src.exception.custom_exception import ProjectException
from src.components.tokenizer import Tokenizer
import sys

try:
    data =  """
    
    C. Subramania Bharati[a] (born C. Subramaniyan 11 December 1882 – 11 September 1921) was an Indian writer, poet, journalist, teacher, 
    Indian independence activist, social reformer and polyglot. 
    He was bestowed the title Bharati for his poetry and was a pioneer of modern Tamil poetry. 
    He is popularly known by his title Bharati or Bharathiyaar and also by the other title "Mahakavi Bharati" ("the great poet Bharati"). 
    His works included patriotic songs composed during the Indian Independence movement. He fought for the emancipation of women, against child marriage, 
    opposed the caste system, and advocated reforms of the society and religion.

    Born in Ettayapuram of Tirunelveli district (present-day Thoothukudi) in 1882, Bharati had his early education in Tirunelveli.
    He later lived in Varanasi for sometime where he was exposed to Hindu theology and new languages. He worked as a journalist with many newspapers, 
    including Swadesamitran, The Hindu, Bala Bharata, Vijaya, Chakravarthini and India. 
    He considered Sister Nivedita, a disciple of Swami Vivekananda, as his guru.

    In 1908, the British Government issued an arrest warrant for Bharathi which pushed him to live in exile in the French-controlled Pondicherry for about ten years until 1918. 
    He was attacked by an Indian elephant at Thiruvallikeni Parthasarathy Temple whom he fed daily and died a few months later on 11 September 1921.
    Bharthi was well-versed in several languages and had a passion for Tamil. His works covered political, 
    social and spiritual themes. Songs and poems composed by Bharthi are used in Tamil literature, music and daily life.
    His works include Panjali Sabatham, Kannan Paatu, Kuyil Paatu, Paapa Paatu, Chinnanchriu Kiliye, 
    Vinayagar Nanmanimalai and Tamil translations of Patanjali's Yoga Sutra and Bhagavat Gita. 
    Bharathi was the first poet whose literature was nationalized in 1949.  
    """
    if data:
        tokenizer = Tokenizer()
        encoded_ids ,merges = tokenizer.encoder(sentence=data )
        print(tokenizer.decode(encoded_ids))
    else:
        print("No data")
except Exception as e:
    ProjectException(e,sys)