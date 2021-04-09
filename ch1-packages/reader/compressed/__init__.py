from reader.compressed.bzipped import opener as bz2_opener
from reader.compressed.gzipped import opener as gzip_opener

# only allow importing these symbols when * imported
__all__ = ['bz2_opener', 'gzip_opener']