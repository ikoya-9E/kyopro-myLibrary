class UnionFind:
  def __init__(self,n):
    self.n=n
    self.par=[-1]*n
    self.siz=[1]*n
  
  def root(self,x):
    while True:
      if self.par[x]==-1:
        break
      x=self.par[x]
    return x
  
  def unite(self,u,v):
    RootU=self.root(u)
    RootV=self.root(v)
    if RootU==RootV:
      return
    if self.siz[RootU]<self.siz[RootV]:
      self.par[RootU]=RootV
      self.siz[RootV]=self.siz[RootU]+self.siz[RootV]
    else:
      self.par[RootV]=RootU
      self.siz[RootU]=self.siz[RootU]+self.siz[RootV]
  
  def same(self,u,v):
    if self.root(u)==self.root(v):
      return True
    else:
      return False
      
  def size(self,x):
    return self.siz[self.root(x)]