### PCR PRIMER DESIGN TEST

### Determining sequence length
def seq_length(seq_name, seq_identity):
    print("Your " + seq_name + " is " + str(len(seq_identity)) + " bases long.")

### Determining GC content
def gc_content(seq_name, seq_identity):
    g_cont = seq_identity.count("G")
    c_cont = seq_identity.count("C")
    print("The GC content of your " + seq_name + " is " + str((seq_identity.count("G") + seq_identity.count("C")) / len(seq_identity) * 100) + " %.")
    
### Determining GC clamp
def gc_clamp(seq_name, seq_identity):
    gc_cont = seq_identity[-5:].count("G") + seq_identity[-5:].count("C")
    if gc_cont == 0:
        return print("There is no GC clamp present for your " + seq_name + ".")
        return print("GC clamp present for " + seq_name + ".")
    elif gc_cont > 3:
        return print("The GC content at 3' end of your " + seq_name + " is too high.")
    else:
         return print("GC clamp present for " + seq_name + ".")
        

sequence = input("Please input sequence of interest without any gaps: ").upper()
seq_length("sequence", sequence)
gc_content("sequence", sequence)

primer_f = input("Please input the sequence for your forward primer: ").upper()
seq_length("forward primer", primer_f)
gc_content("forward primer", primer_f)
gc_clamp("forward primer", primer_f)

primer_r = input("Please input the  reverse complement sequence for your reverse primer: ").upper()
seq_length("reverse primer", primer_r)
gc_content("reverse primer", primer_r)
gc_clamp("reverse primer", primer_r)

### Determining amplicon length
len_amp = (sequence.index(primer_r) + 1) + len(primer_r) - (sequence.index(primer_f) + 1)
print("Your amplicon is " + str(len_amp) + " bases long.")
