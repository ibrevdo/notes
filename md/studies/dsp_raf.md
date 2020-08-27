---
order: 4

---

# DSP

#### Signal representation
_x_ is a vector

_x_ = (X0, X1, X2, ... Xn, ...)

#### Axes
Regular Axis
_x_ = (1,3) = 1(1,0) + 3(0,1)


Axes rotation
_x_=(1,3) = (a,b)

#### Inner product

_x_ = (X0,...Xn-1), _y_ = (Y0, ..., Yn-1)

(_x_,_y_) = SUM(Xn,Yn) when n=0 to N-1

Angle between two vectors:
cos(teta)=(_x_,_y_)/ (||x|| ||y||) 
teta is angle betwwen two vectors 
when: ||x||^2 = SUM(Xi^2), i=0 to N-1 (Norma of _x_)

Parallel vectors : teta = 0, cos(teta) = 1
xIy , teta = pi/2 , cos(teta) = 0
if vectors are normalized, (x,y) = cos(teta)

#### Projection
a - is a projection of vector _x_ on _y_
a = ||x|| cos(teta)


#### Complex numbers

z = a + jb = r * e^j@ 
= r * cos(@) + j * r * sin(@) 
(@ - angle of complex number)

sine wave:
@=2 * pi * f * t, r * e^j2pi * ft = r * cos(2pi * ft)+jsin(2pi * ft)

conjugate:
z * = a-jb = r * e^-j@

#### Choosing best axes (Fourier transform)

coordinate a = (x(t), f(t)) = integral(x(t) * f(t) * ) \\
sine wave basis: f(t) = e^j2pi * ft \\
X(f) = integral( x(t) * e^-j2pi * ft)


#### Fourier transform



#### Spectrum of digital signal


## System representation 


## Multi-Rate Systems 

Xn - @F, signal sampled with rate F \\
Decimator M:1 - Down-Sampler \\
Ym - @F/M, signal down sampled by rate M


Xn - @F, signal sampled with rate F \\
Interpolator 1:L - Up-Smapler \\
Ym - @FL, signal up-sampled with rate FL


## DFT and FFT 

### DFT

<m>X k =sum{n=0}{N-1}{xn e^(( - j 2 pi t)/N n k)}     k=0,..,N-1</m>

DFT is sampling of the windowed spectrum with resolution F/N

interpolation in frequency

how to increase frequency resolution from F/N to F/M, M>N

enlarge signal to M samples (padding)
x0..xN-1,0..0

do DFT on it



