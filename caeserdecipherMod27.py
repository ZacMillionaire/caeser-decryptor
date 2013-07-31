############
#
# Caeser decryptor for mod 27
#
# By Scott Schultz
#
# Takes a string encrypted with mod 27 (a-z including space), determains if any common english trigrams exist based on a shift,
# and returns the shift used to encrypt it if a trigram is found then returns the decrypted message.
#
# If no trigrams are found the most common letter is dropped and the process repeats until a trigram is found or the list is exhausted.
#
# This script assumes the encryption was performed including spaces, and void of symbols.
#
# Of course almost 0 people on the internet actually provide the means to encrypt with a custom dictionary assuming A = 0 and _ = 27,
# so this is a very specific decryptor.
#
# To test, enter the following as the encrypted string: OC_VAWDGPM_VHWTVX_VXJOCVZ_GDX_MWO_VWIZVYGWIZ_NODI_
#
############

class DecryptString:

    decrypted_string = ''
    common_trigrams = ['_TH','ION','ND_','AND','_AN','THE','TIO','IN_','ENT','HE_','___','MEN','AL_','ATI','OF_','_OF','ON_','ING','_CO','ES_','NG_','TO_','PRO','_TO']
    
    def __init__(self, character_chart):
        top_character = character_chart[:1]
        print "> Most common character found was: %s with %d occurances. %s is at position %d" %(top_character[0][0],top_character[0][1],top_character[0][0],(encryption_dictionary.index(top_character[0][0])+1))
        shift = encryption_dictionary.index(top_character[0][0])+1
        print "> shift from _ to %s is %d" %(top_character[0][0],shift)
        for letter in encrypted_string:
            curr_index = encryption_dictionary.index(letter)
            new_letter_index = curr_index - shift
            self.decrypted_string = self.decrypted_string+encryption_dictionary[new_letter_index]

        if self.findCommonWords() == True:
            print "> Found a match!"
            print "> The message is most likely: %s with a shift of %d." %(self.decrypted_string,shift)
        else:
            character_chart.pop(0)
            print "> No match, dropping the last letter used (%s)" %(top_character[0][0])
            DecryptString(character_chart)
            
    def findCommonWords(self):
        print "> Now looking for common trigrams within %s..." %(self.decrypted_string)
        for trigram in self.common_trigrams:
            if self.decrypted_string.find(trigram) != -1:
                return True

encrypted_string = raw_input("Please enter the Caeser encrypted string: ").strip().upper()
encryption_dictionary = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'

occurance_table = {}
for letter in range(len(encryption_dictionary)):
    letter_search = encrypted_string.count(encryption_dictionary[letter])
    occurance_table[encryption_dictionary[letter]] = letter_search

character_chart = sorted(occurance_table.items(),key=lambda x: x[1],reverse=True)
print "Attempting to decrypt: %s..." %(encrypted_string)
decrypted_string = DecryptString(character_chart)
