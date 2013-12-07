Summary:	Test pages to check the output quality of printers
Name:		printer-testpages
Version:	2013
Release:	3
License:	GPLv2
Group:		Publishing
Url:		%{disturl}
# (tpg) Based on Wayne Sallee work
# https://issues.openmandriva.org/show_bug.cgi?id=219
Source0:	printer-testpages-2013.tar.xz
BuildArch:	noarch
BuildRequires:	transfig

%description -n printer-testpages
These are sample files to check the output quality of printers. Thers
is the CUPS test page with colour gradients, the Red Hat test page
with image position checks, a photo test page and a text test page.

%prep
%setup -q

%build
# CUPS test page
cat testprint.prolog.ps.in OMDLINUX-ps1.eps testprint.epilog.ps.in > testprint.ps
# Red Hat test pages: Generate PS files of the XFig drawings
fig2dev -Lps -zLetter testpage.fig testpage.ps
fig2dev -Lps -zA4 testpage-a4.fig testpage-a4.ps

%install
install -d %{buildroot}%{_datadir}/%{name}
install -m 644  *.ps *.jpg *.asc %{buildroot}%{_datadir}/printer-testpages

%files
%{_datadir}/printer-testpages

