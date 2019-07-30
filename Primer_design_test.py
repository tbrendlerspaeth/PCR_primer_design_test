### PCR PRIMER DESIGN TEST

### Determining sequence length
def seq_length(seq_name, seq_identity):
    print("Your " + seq_name + " is " + str(len(seq_identity)) + " bases long.")

### Determining GC clamp
def gc_clamp(seq_name, seq_identity):
    gc_count_clamp = seq_identity[-5:].count("G") + seq_identity[-5:].count("C")
    if gc_count_clamp == 0:
        return print("There is no GC clamp present for your " + seq_name + ".")
    elif gc_count_clamp > 3:
        return print("The GC content at 3' end of your " + seq_name + " is too high.")
    else:
         return print("GC clamp present for " + seq_name + ".")
        
# Primer melting temperature, according to formula Tm = 4(G+C) + 2(A+T)
def primer_tm(seq_name, gc_count, seq_identity):
        tm = 4*gc_count + 2*(len(seq_identity) - gc_count)
        print("The melting temperature of your " + seq_name + " is " + str(tm) + " degrees Celsius.")
    
temp_seq = input("Please enter your template sequence without any gaps: ").upper()

primer_f = input("Please enter the sequence for your forward primer: ").upper()
seq_length("forward primer", primer_f)
gc_count_primer_f = primer_f.count("G") + primer_f.count("C")
print("The GC content of your forward primer is " + str(gc_count_primer_f / len(primer_f) * 100) + "%.")
gc_clamp("forward primer", primer_f)
primer_tm("forward primer", gc_count_primer_f, primer_f)

primer_r = input("Please enter the reverse complement sequence for your reverse primer: ").upper()
seq_length("reverse primer", primer_r)
gc_count_primer_r = primer_r.count("G") + primer_r.count("C")
print("The GC content of your reverse primer is " + str(gc_count_primer_r / len(primer_r) * 100) + "%.")
gc_clamp("reverse primer", primer_r)
primer_tm("reverse primer", gc_count_primer_r, primer_r)

### Determining amplicon length
len_amp = (temp_seq.index(primer_r) + 1) + len(primer_r) - (temp_seq.index(primer_f) + 1)
print("Your amplicon is " + str(len_amp) + " bases long.")
