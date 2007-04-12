%define version 2006
%define release 1mdk

##### RPM PROBLEM WORKAROUNDS

# Suppress automatically generated Requires for Perl libraries.
#define _requires_exceptions perl\(.*\)

#define _unpackaged_files_terminate_build       0 
#define _missing_doc_files_terminate_build      0


Summary: Test pages to check the output quality of printers
Name:		printer-testpages
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Publishing
URL:		http://www.mandriva.com/
BuildArchitectures: noarch

##### PRINTER TESTPAGES BUILDREQUIRES

BuildRequires:	transfig

##### PRINTER TESTPAGES SOURCES

# Mandrivized printer test pages (originals from CUPS and Red Hat)
Source300:	mdk-testpages.tar.bz2
# Photo test page from Gimp-Print and ESP GhostScript
Source302:	cups-profile.jpg.bz2

##### BUILD ROOT

BuildRoot:	%_tmppath/%name-%version-%release-root

##### PACKAGE DESCRIPTION

%description -n printer-testpages
These are sample files to check the output quality of printers. Thers
is the CUPS test page with colour gradients, the Red Hat test page
with image position checks, a photo test page and a text test page.



%prep
# remove old directory
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
mkdir $RPM_BUILD_DIR/%{name}-%{version}

# Red Hat test pages
%setup -q -T -D -a 300 -n %{name}-%{version}

# Photo test page
bzcat %{SOURCE302} > $RPM_BUILD_DIR/%{name}-%{version}/photo-testpage.jpg



%build

cd $RPM_BUILD_DIR/%{name}-%{version}

# Mandrivized CUPS test page
cat testprint.prolog.ps.in MDALINUX-ps1.eps testprint.epilog.ps.in > testprint.ps

# Red Hat test pages: Generate PS files of the XFig drawings
fig2dev -Lps -zLetter testpage.fig testpage.ps
fig2dev -Lps -zA4 testpage-a4.fig testpage-a4.ps



%install

rm -rf $RPM_BUILD_ROOT

# Make directory
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cd $RPM_BUILD_DIR/%{name}-%{version}

cp *.ps *.jpg *.asc $RPM_BUILD_ROOT%{_datadir}/printer-testpages



##### FILES

%files
%defattr(-,root,root)
%{_datadir}/printer-testpages



%clean
rm -rf $RPM_BUILD_ROOT

