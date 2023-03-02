# Generátor projektu 1 do IZU

Ukázka použití: (koukněte se do zdrojáku kde je seznam proměnných a nad nima komentář co do nich dát)

```python
import izu_proj1_generator.izu_proj1_generator as gen
gen.name = "Příjmení Jméno"
# ...
print(gen.get_latex())
```

Následně stačí hodit vygenerovaný LaTeX do Overleafu a vygenerovat si PDF.