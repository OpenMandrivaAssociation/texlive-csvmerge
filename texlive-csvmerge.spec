Name:		texlive-csvmerge
Version:	51857
Release:	2
Summary:	Merge TeX code with csv data
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/csvmerge
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csvmerge.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csvmerge.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csvmerge.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros for processing a csv spreadsheet
file with a minimum of configuration for the csv file. The
first row names the columns and the remaining rows are data.
This data can be merged with TeX code residing in an auxiliary
file and the process repeated for each data row. There is one
macro to set things up, one to extract the data, and one to
tell if the field is empty or not. The documentation contains
examples.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/csvmerge
%{_texmfdistdir}/tex/latex/csvmerge
%doc %{_texmfdistdir}/doc/latex/csvmerge

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
