Summary:	American English male voice 'kal'
Summary(pl.UTF-8):	Amerykańska odmiana języka angielskiego - głos męski 'kal'
Name:		festival-vox-kallpc
Version:	0.1
Release:	3
License:	distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festvox_kallpc16k.tar.gz
# Source0-md5:	abbd12e1d04ecdcae07f1d0044f3a947
Requires:	festival-lex-CMU
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This voice provides an American English male voice using a residual
excited LPC diphone synthesis method. It uses the CMU Lexicon
pronunciations. Prosodic phrasing is provided by a statistically
trained model using part of speech and local distribution of breaks.
Intonation is provided by a CART tree predicting ToBI accents and an
F0 contour generated from a model trained from natural speech. The
duration model is also trained from data using a CART tree.

%description -l pl.UTF-8
Ten pakiet udostępnia głos męski dla amerykańskiej odmiany języka
angielskiego. Używa wzbudzanej szczątkowo dwugłoskowej metody syntezy
LPC. Używa leksykonu wymowy CMU. Frazy prozodyczne są zapewnione
przez statystycznie nauczony model przy użyciu części mowy i lokalnego
rozłożenia przerw. Intonację zapewnia drzewo CART przewidujące akcenty
ToBI i obrys F0 generowany z modelu nauczonego na podstawie naturalnej
mowy. Model czasów trwania jest nauczony na podstawie danych z drzewa
CART.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english

cd festival/lib/voices/english
cp -r kal_diphone $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english
rm $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english/kal_diphone/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc festival/lib/voices/english/kal_diphone/COPYING
%{_datadir}/festival/lib/voices/english/kal_diphone
