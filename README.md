# typeswap

Swap variable types fast!

## usage
To swap your variable type, simply import typeswap like
`import typeswap` or `from typeswap import changetype`
then run the changetype function like so: `changetype(variable, newtype)`
valid newtypes are:
    - "string"
    - "float"
    - "int"
and variable will be the original value to change.

## example
```python
import typeswap

string = "1"
int = typeswap.changetype(string, "int")
print(int) 
```