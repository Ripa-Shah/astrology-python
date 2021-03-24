{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "tracked-football",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Aqr', 'Aquarius')\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-1-f67670363648>:3: DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats\n",
      "  print(ephem.constellation(m))\n"
     ]
    }
   ],
   "source": [
    "import ephem\n",
    "m=ephem.Mars('1970')\n",
    "print(ephem.constellation(m))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "appropriate-fitting",
   "metadata": {},
   "outputs": [],
   "source": [
    " m = ephem.Mars()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fitting-conducting",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Mars'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m.name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "medieval-content",
   "metadata": {},
   "outputs": [],
   "source": [
    " a = ephem.star('Arcturus')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "right-catholic",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Arcturus'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "double-sugar",
   "metadata": {},
   "outputs": [],
   "source": [
    "m = ephem.Mars('2003/8/27')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "positive-facility",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mars -173:00:34.2 25.1121063232\n"
     ]
    }
   ],
   "source": [
    " print('%s %s %.10f' % (m.name, m.elong, m.size))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "soviet-rogers",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Observer' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-9-dd841e0154aa>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m#Define observer location\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mgatech\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mObserver\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[0mgatech\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlon\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'-3.0'\u001b[0m \u001b[1;31m#Longitude positive in the East\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mgatech\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlat\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'+51.0'\u001b[0m \u001b[1;31m#Latitude positive in the North\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Observer' is not defined"
     ]
    }
   ],
   "source": [
    "star = ephem.FixedBody(ra='21:00:00', dec='-20:00:00')\n",
    "\n",
    "#Define observer location\n",
    "gatech = Observer()\n",
    "gatech.lon = '-3.0' #Longitude positive in the East\n",
    "gatech.lat = '+51.0' #Latitude positive in the North\n",
    "gatech.elevation = 0 \n",
    "\n",
    "#Set date of observation and then prints Altitude and Azimuth of object\n",
    "gatech.date = ((2000, 1, 1, 9, 30, 0)) #Year,month,day,hour,minute,second\n",
    "\n",
    "v1 = Venus(gatech)\n",
    "v1altrad = ('%.12f' % float(v1.alt))\n",
    "v1azrad = ('%.12f' % float(v1.az -3.14159))\n",
    "star.compute(gatech)\n",
    "print(star.alt, star.az)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "insured-designation",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "homeless-buying",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[#################################] 100% de421.bsp\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "04h 38m 19.24s\n",
      "+23deg 36' 15.9\"\n",
      "1.68611 au\n"
     ]
    }
   ],
   "source": [
    "from skyfield.api import load\n",
    "\n",
    "planets = load('de421.bsp')\n",
    "earth, mars = planets['earth'], planets['mars']\n",
    "\n",
    "ts = load.timescale()\n",
    "t = ts.now()\n",
    "astrometric = earth.at(t).observe(mars)\n",
    "ra, dec, distance = astrometric.radec()\n",
    "\n",
    "print(ra)\n",
    "print(dec)\n",
    "print(distance)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "maritime-nickel",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'solarsystem'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-11-f29b4c785bac>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;31m# import math\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0msolarsystem\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;31m# import planetview\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;31m# from libraries.planetview import solarsystem\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'solarsystem'"
     ]
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "# import math\n",
    "import datetime\n",
    "import solarsystem\n",
    "# import planetview\n",
    "# from libraries.planetview import solarsystem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "bound-custom",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LocationInfo(name='London', region='England', timezone='Europe/London', latitude=51.473333333333336, longitude=-0.0008333333333333334)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from astral.geocoder import database, lookup\n",
    "lookup(\"London\", database())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "appreciated-indicator",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-24-c34768bbd69d>:4: DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats\n",
      "  ephem.constellation(sun)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "('Psc', 'Pisces')"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import ephem\n",
    "sun = ephem.Sun()\n",
    "sun.compute('2021/03/23 17:14:39')\n",
    "ephem.constellation(sun)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "intimate-poland",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-25-f4094ca33a41>:3: DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats\n",
      "  ephem.constellation(mars)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "('Tau', 'Taurus')"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars=ephem.Mars()\n",
    "mars.compute('2021/03/23 17:21:51')\n",
    "ephem.constellation(mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "centered-rochester",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-26-6ebf0058531b>:3: DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats\n",
      "  ephem.constellation(venus)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "('Psc', 'Pisces')"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "venus=ephem.Venus()\n",
    "venus.compute('2021/03/23 17:21:51')\n",
    "ephem.constellation(venus)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "checked-desert",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-27-791838d8accc>:3: DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats\n",
      "  ephem.constellation(mercury)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "('Aqr', 'Aquarius')"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mercury=ephem.Mercury()\n",
    "mercury.compute('2021/03/23 17:23:55')\n",
    "ephem.constellation(mercury)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "becoming-tsunami",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-28-24bc1fb45453>:3: DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats\n",
      "  ephem.constellation(saturn)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "('Cap', 'Capricornus')"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "saturn=ephem.Saturn()\n",
    "saturn.compute('2021/03/21 17:25:16')\n",
    "ephem.constellation(saturn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "unavailable-filename",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-30-bfc22612d9da>:3: DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats\n",
      "  ephem.constellation(jupiter)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "('Cap', 'Capricornus')"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jupiter=ephem.Jupiter()\n",
    "jupiter.compute('2021/03/21 17:26:37')\n",
    "ephem.constellation(jupiter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "described-rates",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-31-aedeef143f66>:3: DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats\n",
      "  ephem.constellation(moon)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "('Gem', 'Gemini')"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "moon=ephem.Moon()\n",
    "moon.compute('2021/03/21 17:27:29')\n",
    "ephem.constellation(moon)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "brief-blame",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
