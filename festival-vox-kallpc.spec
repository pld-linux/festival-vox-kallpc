Summary:	American English male voice 'kal'
Summary(pl):	Amerykañska odmiana jêzyka angielskiego - g³os mêski 'kal'
Name:		festival-vox-kallpc
Version:	0.1
Release:	1
License:	Distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festvox_kallpc16k.tar.gz
Requires:	festival-lex-CMU
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This voice provides an American English male voice using a residual
excited LPC diphone synthesis method. It uses the CMU Lexicon
pronunciations. Prosodic phrasing is provided by a statistically
trained model using part of speech and local distribution of breaks.
Intonation is provided by a CART tree predicting ToBI accents and an
F0 contour generated from a model trained from natural speech. The
duration model is also trained from data using a CART tree.

%prep
%setup -q -c %{name}-%{version}

%build

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
